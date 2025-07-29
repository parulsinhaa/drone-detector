from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # You can also try yolov8s.pt for better accuracy

# Train on your custom dataset
model.train(
    data="data.yaml",         # Make sure this file exists in your folder
    epochs=20,                # You can increase for better results
    imgsz=640,                # Input image size
    batch=8,                  # Change based on your RAM
    project="drone_project",  # Output folder
    name="yolo_drone_model"   # Run name
)
