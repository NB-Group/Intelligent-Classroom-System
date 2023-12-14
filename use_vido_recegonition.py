from config import *
import time
import cv2
import tensorflow as tf
import numpy as np
import requests
import sys
from PIL import Image
import os
import face_recognition
import xlwings as xw
import atexit
import keras

# --init--
print("正在初始化表格")
app = xw.App(visible=True, add_book=False)
wb = app.books.open(r'./test.xlsx')

for i in range(len(face_names)):
    wb.sheets['sheet1'].range(f'A{i + 1}').value = face_names[i]

# 行号
letters = []
for i in range(26):
    letters.append(chr(ord("A") + i))

print("正在初始化变量")

file_name = "./test_data/nb.jpg"

IS_DRR = True
IS_SaveIMG = False

print("抓取视频流：", end="")
cap = cv2.VideoCapture('./test_data/nb.mp4')
print("成功")
# 加载模型
print("加载CNN模型")
model = keras.models.load_model('./model/model2.0.keras')


# --functions--
@atexit.register
def clean():
    # wb.save()
    wb.close()
    app.quit()


def gesture_recognition(path):
    img = keras.utils.load_img(
        path, target_size=(112, 112)
    )
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return class_names[np.argmax(score)], 100 * np.max(score)


def image_segmentation(path):
    with open(path, "rb") as f:
        response = requests.post(url, headers=headers, data=data, files={"image": f})

    # Check for successful response
    response.raise_for_status()
    return response.json()


x = 2

if __name__ == "__main__":
    if "-NoDRR" in sys.argv:
        IS_DRR = False
    if "-SaveIMG" in sys.argv:
        IS_SaveIMG = True
    print("开始执行--")
    while True:
        time_global = time.time()
        for i in range(30):
            ret, frame = cap.read()
        cv2.imshow("A video", frame)
        cv2.imwrite(file_name, frame)

        image = Image.open(file_name)
        image_backups = image

        res = image_segmentation(file_name)
        objects = res['data']

        for i, obj in enumerate(objects):

            t = time.time()
            box = obj['box']
            if obj['name'] != 'person':
                continue
            cropped_image = image_backups.crop((box['x1'], box['y1'], box['x2'], box['y2']))
            cropped_image.save(f'./img/cropped_{i}.jpg')

            class_name, confidence = gesture_recognition(f'./img/cropped_{i}.jpg')

            picture = face_recognition.load_image_file(f'./img/cropped_{i}.jpg')
            try:
                encoding = face_recognition.face_encodings(picture)[0]
            except IndexError as e:
                print("没有人脸")
            cv2.putText(frame,
                        class_name,
                        (int(box['x1']), int(box['y1']) + 30),
                        font, 1, (255, 255, 255), 1)

            try:
                res = face_recognition.face_distance(face_encodings_list, encoding)
                face_name = face_names[np.argmin(res)]
                print(
                    f"图片中的第{i}张人像：人名={face_name},行为={class_name},行为置信度={confidence},人像处理用时:{time.time() - t}")
                face_index = face_names.index(face_name)
                wb.sheets['sheet1'].range(f'{letters[x - 1]}{face_index + 1}').value = class_name
                if IS_DRR:
                    cv2.putText(frame,
                                face_name,
                                (int(box['x1']), int(box['y1']) + 60),
                                font, 1, (255, 255, 255), 1)

            except Exception as e:
                pass

            if not IS_SaveIMG:
                os.remove(f'./img/cropped_{i}.jpg')
                pass
            if IS_DRR:
                cv2.rectangle(frame, (int(box['x1']), int(box['y1'])), (int(box['x2']), int(box['y2'])),
                              (255, 255, 255), 1)
        x += 1
        if IS_DRR:
            img_test1 = cv2.resize(frame, (int(frame.shape[0] / 2), int(frame.shape[1] / 2)))
            cv2.imwrite(f"./debug/test{x}   .jpg",frame)
            cv2.imshow("A video", frame)
        print(time_global - time.time())
        c = cv2.waitKey(1)
        if c == 27:
            break

    cv2.destroyAllWindows()
