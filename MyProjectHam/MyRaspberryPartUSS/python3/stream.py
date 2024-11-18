import io
from picamera2 import Picamera2
from flask import Flask, Response
import cv2

app = Flask(__name__)

def generate_frames():
    try:
        camera = Picamera2()
        camera.configure(camera.create_video_configuration(main={"size": (320, 240), "format": "RGB888"}))
        camera.start()

        while True:
            # Capture frame as a numpy array
            frame = camera.capture_array()
            print("Frame captured")

            # Encode the frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', frame)
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
