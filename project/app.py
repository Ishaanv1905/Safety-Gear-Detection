from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import os
from flask import Flask, request, send_file, render_template

app = Flask(__name__, template_folder='templates')

model = YOLO(r"C:\Users\Ishaan Verma\Desktop\ACT\VLM-Safety Gear Detection\project\yolo11n.pt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image found", 400
    file = request.files['image']
    image = Image.open(file.stream).convert("RGB")
    image_np = np.array(image)
    results = model.predict(source=image_np, imgsz=640, conf=0.25, verbose=False)
    annotated_frame = results[0].plot()
    _, buffer = cv2.imencode('.jpg', annotated_frame)
    return send_file(io.BytesIO(buffer), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)