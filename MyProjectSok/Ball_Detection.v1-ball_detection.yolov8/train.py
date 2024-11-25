
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # Load a pretrained YOLOv8 nano model (recommended for training)

# Train the model with MPS (Metal Performance Shaders for macOS)
results = model.train(
    data="/Users/sokainacherkane/Desktop/SmarteSystemer/smartesystemer/MyProjectSok/Ball_Detection.v1-ball_detection.yolov8/data.yaml",
    epochs=100,
    imgsz=640,
    device="mps"  # NB. mps brukes for trening på macbook M1 fordi den har bedre performance 
)

