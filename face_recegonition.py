# from config import *
# import time
# import numpy
#
# picture = face_recognition.load_image_file(f'./img/cropped_0.jpg')
# encoding = face_recognition.face_encodings(picture)[0]
#
# t = time.time()
# for tolerance in numpy.arange(0.1,0.6,0.1):
#     flag = False
#     for face_name in face_names:
#         res = face_recognition.compare_faces(face_encodings[face_name], encoding, tolerance=tolerance)
#         try:
#             if res[0]:
#                 flag = True
#                 print("是:", face_name)
#         except Exception as e:
#             pass
#     if flag:
#         break
#
# print(time.time()-t)
import os
import face_recognition
import numpy as np

face_encodings = {}
face_encodings_list = []
face_names = []

directories = [d for d in os.listdir('./face_data/') if os.path.isdir(os.path.join('./face_data/', d))]


def get_name(path, name):
    image = face_recognition.load_image_file(path)
    list_of_face_encodings = face_recognition.face_encodings(image)
    if list_of_face_encodings:
        # Only add non-empty encodings to the lists
        face_encodings[name] = list_of_face_encodings[0]  # Assuming only one face in the image
        face_encodings_list.append(list_of_face_encodings[0])
        face_names.append(name)


for directory in directories:
    file_path = os.path.join('./face_data', directory, '1.jpg')
    get_name(file_path, directory)

picture = face_recognition.load_image_file(f'./img/cropped_20.jpg')
my_face_encoding = face_recognition.face_encodings(picture)[0]

# Calculate face distances using face_recognition.face_distance
distances = face_recognition.face_distance(face_encodings_list, my_face_encoding)

# Set a tolerance threshold for considering a match
tolerance = 0.6

# Find the index of the closest match
min_distance_index = np.argmin(distances)

# Check if the minimum distance is below the tolerance
if distances[min_distance_index] <= tolerance:
    print(face_names[min_distance_index])
else:
    print("No match found")
