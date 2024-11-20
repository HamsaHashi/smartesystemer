import sys
sys.path.append("/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/MyRaspberryPartUSS/yolo_object/lib/python3.11/site-packages")

from ultralytics import YOLO

# Load the PyTorch model
model = YOLO("SokHam.pt")

# Export as an NCNN format
model.export(format="ncnn") 