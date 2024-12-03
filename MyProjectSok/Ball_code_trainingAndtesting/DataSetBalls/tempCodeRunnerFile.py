from roboflow import Roboflow


rf = Roboflow(api_key="IVhM9T78rYu1me4Uqoz3")

project = rf.workspace("yoloballtracking").project("object_tracking")

#her laster jeg ned datasettet: 
dataset = project.version(5).download("yolov8", location="/Users/sokainacherkane/Documents/DataSetBalls") 