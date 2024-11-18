
from ultralytics import YOLO

# Load the PyTorch model
model = YOLO("SokHam.pt")

# Export as an NCNN format
model.export(format="ncnn") 