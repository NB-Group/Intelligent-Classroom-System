import face_recognition
import os

# 获取"./data"目录下的所有目录名
directories = [d for d in os.listdir('./face_data/') if os.path.isdir(os.path.join('./face_data/', d))]

print(directories)
face_encodings = {}


def get_name(path, name):
    image = face_recognition.load_image_file(path)
    list_of_face_encodings = face_recognition.face_encodings(image)
    face_encodings[name] = list_of_face_encodings
    print(f"{name}的人类数据完成")


for directory in directories:
    file_path = os.path.join('./face_data', directory, '1.jpg')
    get_name(file_path, directory)
