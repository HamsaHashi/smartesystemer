import io
from picamera2 import Picamera2
from flask import Flask, Response
import cv2
import numpy as np
import time

app = Flask(__name__)

# Initialize the camera
camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"size": (320, 240), "format": "RGB888"}))
camera.start()

def generate_frames():
    try:
        while True:
            # Capture frame as a numpy array
            frame = camera.capture_array()
            # Resize or downsample the frame if needed for faster processing
            frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_LINEAR)

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])  # Reduce quality for speed
            if not ret:
                print("Failed to encode frame")
                continue

            # Yield frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
    except Exception as e:
        print("Error in generate_frames:", e)

@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
