from picamera2 import Picamera2
from flask import Flask, Response, request
from datetime import datetime
import cv2

app = Flask(__name__)

# Initialiser kameraet
camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"size": (960, 720), "format": "RGB888"}))
camera.start()

@app.route('/')
def index():
    return """
    <h1>Raspberry Pi Camera Stream</h1>
    <p>Du kan se strømmen på /video_feed og ta bilde med en POST-forespørsel til /capture.</p>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    camera.stop()
    camera.still_configuration.main.size = (2592, 1944)
    camera.still_configuration.main.format = "RGB888"
    camera.configure("still")
    camera.start()

    # Lagre bildet med tidsstempel
    filename = f"/home/hamsahashi/Downloads/capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    camera.capture_file(filename)
    print(f"Høyoppløselig bilde lagret som {filename}")

    # Gå tilbake til lavere oppløsning for streaming
    camera.stop()
    camera.configure(camera.create_video_configuration(main={"size": (960, 720), "format": "RGB888"}))
    camera.start()

    return ('', 204)

def generate_frames():
    while True:
        frame = camera.capture_array()
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
