from ultralytics import YOLO

# Load model
model = YOLO(r"C:\Users\Ishaan Verma\Desktop\ACT\VLM-Safety Gear Detection\project\yolo11n.pt")

# Run inference on folder of images
results = model.predict(
    source=r"C:\Users\Ishaan Verma\Desktop\ACT\VLM-Safety Gear Detection\project\test_images",
    imgsz=640,
    conf=0.25
)

# Visualize results
for r in results:
    r.show()
