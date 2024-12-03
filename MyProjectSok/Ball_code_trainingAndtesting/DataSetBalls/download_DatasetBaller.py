#her er bildene importert fra roboflow som jeg lagde (egen bruker) etter annotering av hver bilde;, nå importeres ferdig annoterte bilder for å starte treningen og deretter testingen. 

from roboflow import Roboflow

print("Initializing Roboflow...")
rf = Roboflow(api_key="IVhM9T78rYu1me4Uqoz3")
print("Loading workspace...")
project = rf.workspace("yoloballtracking").project("object_tracking")
print("Accessing dataset version...")
dataset = project.version(5).download("yolov8", location="/Users/sokainacherkane/Documents/DataSetBalls")
print("Download complete!")
