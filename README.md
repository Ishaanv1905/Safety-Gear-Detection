
#  Safety Gear Detection System

A real-time PPE (Personal Protective Equipment) detection system for field engineers and technicians using YOLOv11 and Flask. 

This project captures live video, detects safety gear like helmets and vests, and displays the results via a simple browser interface.


## 📌 Features

- Real-time safety gear detection using webcam input(under 3s)
- Returns annotated images with detected safety gear
- YOLOv11-based object detection
- Flask-based API for image processing
- Simple HTML/JavaScript frontend to capture and stream frames



## Tech Stack

**Backend:** Python, Flask

**Model:** YOLOv11 (ultralytics)

**Frontend:** HTML, JavaScript

**Libraries:** OpenCV, NumPy, Pillow


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ishaanv1905
cd safety-gear-detection
```
### 2. Set up a virtual environment
```bash
python -m venv venv
venv\Scripts\activate          # On Windows
source venv/bin/activate       # On macOS/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
source venv/bin/activate       # On macOS/Linux
```
### 4. Run the Flask app
```bash
python app.py
```

### 5.Open the web app
Open your browser and go to:
http://localhost:5000 
## Authors
**Ishaan Verma**
- Github profile: [@Ishaanv1905](https://github.com/Ishaanv1905)
- LinkedIn: [@IshaanVerma](https://www.linkedin.com/in/ishaan-verma-a834b1305/)
