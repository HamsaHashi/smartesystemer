
from picamera2 import Picamera2

def setup_camera():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (960, 720)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()
    return picam2
