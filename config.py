import face_recognition
import os
import time
import tqdm
import cv2

tags_to_names = {0: "drink", 1: "listen", 2: "trance", 3: "write"}
class_names = ['drink', 'listen', 'trance', 'write']
url = "https://api.ultralytics.com/v1/predict/R6nMlK6kQjSsQ76MPqQM"
headers = {"x-api-key": "你自己的key"}
# daa17fbe445f42dbab18a57970faa17ae0c0ea5947
data = {"size": 640, "confidence": 0.25, "iou": 0.45}
font = cv2.FONT_HERSHEY_SIMPLEX

# 获取"./data"目录下的所有目录名
directories = [d for d in os.listdir('./face_data/') if os.path.isdir(os.path.join('./face_data/', d))]

print(directories)
time.sleep(0.1)

face_encodings = {}
face_encodings_list = []
face_names = []


def get_name(path, name):
    image = face_recognition.load_image_file(path)
    list_of_face_encodings = face_recognition.face_encodings(image)
    try:
        face_encodings[name] = list_of_face_encodings[0]
        face_encodings_list.append(list_of_face_encodings[0])
        face_names.append(name)
    except:
        print(name, "这个人没有脸")


pbar = tqdm.tqdm(total=35, unit="人")

print("正在加载人脸数据")
for directory in directories:
    time_od = time.time()
    file_path = os.path.join('./face_data', directory, '1.jpg')
    get_name(file_path, directory)
    pbar.set_description("为人脸创建编码")
    pbar.update(1)
    pbar.set_postfix({"名称": f"{directory} 创建编码成功", "耗时": f"{time.time() - time_od} MS"})

pbar.close()
print("人脸数据加载完成！")
