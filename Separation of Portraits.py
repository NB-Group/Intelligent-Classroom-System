import requests
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Run inference on an image
url = "https://api.ultralytics.com/v1/predict/R6nMlK6kQjSsQ76MPqQM"
headers = {"x-api-key": "daa17fbe445f42dbab18a57970faa17ae0c0ea5947"}
data = {"size": 640, "confidence": 0.25, "iou": 0.45}
with open("data.jpg", "rb") as f:
    response = requests.post(url, headers=headers, data=data, files={"image": f})

# Check for successful response
response.raise_for_status()

data = response.json()

objects = data['data']

# 打开图片
image = Image.open('data.jpg')
draw = ImageDraw.Draw(image)

# 在图片上标注结果并切割图片
for i, obj in enumerate(objects):
    if obj["name"] != "person":
        continue
    box = obj['box']
    draw.rectangle((box['x1'], box['y1'], box['x2'], box['y2']), outline="red",width=2)

plt.imshow(image)
plt.show()
