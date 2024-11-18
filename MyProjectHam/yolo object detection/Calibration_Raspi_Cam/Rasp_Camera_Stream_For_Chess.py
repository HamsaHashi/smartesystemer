import cv2
from picamera2 import Picamera2
from flask import Flask, Response, render_template_string, request
from datetime import datetime

app = Flask(__name__)

# Initialiser kameraet
camera = Picamera2()

# Konfigurer videooppløsningen til 1440x1080
camera.configure(camera.create_video_configuration(main={"size": (1440, 1080), "format": "RGB888"}))
camera.start()

# HTML for websiden med video-feed
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Raspberry Pi Camera Stream</title>
</head>
<body>
    <h1>Raspberry Pi Camera Stream</h1>
    <img src="/video_feed" width="1440" height="1080">
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    # Bytt til høyoppløsningsmodus for stillbilde, og bruk samme oppløsning som streaming
    camera.stop()
    camera.still_configuration.main.size = (1440, 1080)  # Justert for 1440x1080
    camera.still_configuration.main.format = "RGB888"
    camera.configure("still")
    camera.start()

    # Lagre bildet med tidsstempel
    filename = f"/home/hamsahashi/Downloads/calibration_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    camera.capture_file(filename)
    print(f"Høyoppløselig bilde lagret som {filename}")

    # Gå tilbake til streaming-konfigurasjonen
    camera.stop()
    camera.configure(camera.create_video_configuration(main={"size": (1440, 1080), "format": "RGB888"}))
    camera.start()

    return ('SUKSESS', 204)  # Returnerer en tom respons for å indikere suksess

def generate_frames():
    while True:
        # Capture frame som numpy array
        frame = camera.capture_array()

        # Encode frame som JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        # Send frame som bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

if __name__ == '__main__':
    # Start Flask-serveren
    app.run(host='0.0.0.0', port=8080, threaded=True)
