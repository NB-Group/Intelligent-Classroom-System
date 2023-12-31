# Student Classroom Behavior Detection Project

文档语言|document language

[中文](README_ZH.md)|[[英文]]

This project was developed and written by Haowen Liang (GitHub: @nb_group).

It is a project that utilizes artificial intelligence computer vision technology to detect student behavior in the classroom. It aims to assist teachers in understanding students' learning situations and attention distribution.

## Background
In our educational environment, issues such as students being distracted in class and talking to others have become increasingly serious. In some cases, students even ignore the teacher at the front of the class. In such a complex environment, teachers find it challenging to quickly and accurately identify the person speaking. To address this, I developed a classroom behavior detection system based on artificial intelligence. The system aims to use technological means to help teachers analyze students' learning behavior and provide more data support for teaching effectiveness analysis. With the continuous advancement of technology, artificial intelligence has gradually infiltrated various aspects of our lives. With the assistance of computers, we can efficiently and accurately identify and address discipline disruptions. After incorporating methods such as parental signatures and writing reflections, this system is expected to significantly improve the effectiveness of our class.

## Technical Overview

This project uses [YOLOV8](https://github.com/ultralytics/ultralytics) for image segmentation, separating each student in the classroom scene. The segmented images are then fed into a custom CNN (Convolutional Neural Network) model designed from scratch by Haowen Liang. The model was trained using a dataset collected and annotated by the author, achieving an impressive accuracy of **99.86%**. Lastly, [face_recognition](https://github.com/ageitgey/face_recognition/) is employed for facial recognition.

The behavior detection model can identify the following student behaviors:
- Listening
- Drinking water
- Distracted
- Writing

## User Guide

Although this project is intended for use by our class's teachers, I'll provide a brief tutorial.

Using this project is straightforward, involving the following steps:

1. Clone the project using Git or download the source code directly.
2. Run: `pip install -r requirements.txt`.
3. Register for an Ultralytics account, obtain the deployment API key, and fill it into the `config.py` file.
4. Run `Facial data input.py` and follow the prompts to input facial data.
5. Run `main.py` for real-time camera detection or `use_vido_recegonition.py` to detect using an existing video.
6. Wait for the detection results to be displayed on the screen or saved to the specified folder.

Explanation of directories:
 - `data`: Training data for pose detection model.
 - `debug`: Used for personal debugging.
 - `face_data`: Facial data.
 - `img`: Not necessary for the program, used for debugging. Do not delete.
 - `model`: Behavior detection model.
 - `test_data`: Test data.

This project requires no additional configurations and can run on CPUs. If hardware conditions permit, you can try modifying the code for GPU acceleration, significantly improving speed.

## Open Source License

This project is released under the [GPL v3.0](https://github.com/KSXGitHub/GPL-3.0/blob/89c928a17db494bb6f4c4013d77f5bee076d057d/LICENSE) open-source license. Anyone is free to use, modify, and distribute the project, but they must retain the original author's copyright information and license declaration. Commercial use is strictly prohibited. However, if you want to deploy it at your school, feel free to contact me.
