import tensorflow as tf
from tensorflow.keras.preprocessing import image

import numpy as np
import config

# 加载模型
model = tf.keras.models.load_model('./model/model2.0.keras')

img = tf.keras.utils.load_img(
    "./test.bmp", target_size=(112, 112)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "识别结果 {} | 置信度：{:.2f} %"
    .format(config.class_names[np.argmax(score)], 100 * np.max(score))
)
