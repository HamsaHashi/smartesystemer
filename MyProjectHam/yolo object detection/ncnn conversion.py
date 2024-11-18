
from ultralytics import YOLO

# Load the PyTorch model
model = YOLO("bestNEW.pt")

model.overrides['imgsz'] = 640
# Export as an NCNN format
model.export(format="ncnn") 