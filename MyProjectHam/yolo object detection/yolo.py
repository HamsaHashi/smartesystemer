import cv2
import numpy as np
from picamera2 import Picamera2
from ultralytics import YOLO
import time

class YoloBallDetection:
    def __init__(self, model_path):
        self.model = YOLO(model_path, task='detect')
        self.target_classes = {"Blue_ball": 1, "Green_ball": 2, "Red_ball": 0}  # Juster class_id-er etter din modell

    def detect_ball(self, frame):
        """Detect balls using the YOLO model."""
        results = self.model(frame)
        return results

    def annotate_ball(self, frame, results):
        """Annotate detected balls on the frame using YOLO's built-in method and apply color filtering."""
        annotated_frame = results[0].plot()  # Use built-in method to draw bounding boxes and labels

        # Iterate through detections to apply color filtering
        for box in results[0].boxes:
            confidence = box.conf[0]
            class_id = int(box.cls[0])

            # Check if the detection is one of the target classes and has sufficient confidence
            if confidence >= 0.64 and class_id in self.target_classes.values():
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract coordinates as integers
                class_name = results[0].names[class_id]

                # Extract the region of interest (ROI) for color filtering
                roi = frame[y1:y2, x1:x2]

                # Perform color filtering to confirm the object
                if not self.color_filter(roi, class_name):
                    continue  # Skip this detection if color filtering fails

        return annotated_frame
    def color_filter(self, roi, class_name):
        """Filtrer regionen av interesse (ROI) for å verifisere fargen."""
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Definer fargeområder i HSV for blå, grønn og rød
        if class_name == "Blue_ball":
            lower_bound = np.array([100, 150, 50])
            upper_bound = np.array([140, 255, 255])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
        elif class_name == "Green_ball":
            lower_bound = np.array([35, 100, 50])
            upper_bound = np.array([85, 255, 255])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
        elif class_name == "Red_ball":
            lower_bound1 = np.array([0, 100, 50])
            upper_bound1 = np.array([10, 255, 255])
            lower_bound2 = np.array([170, 100, 50])
            upper_bound2 = np.array([180, 255, 255])
            mask1 = cv2.inRange(hsv, lower_bound1, upper_bound1)
            mask2 = cv2.inRange(hsv, lower_bound2, upper_bound2)
            mask = mask1 | mask2
        else:
            return False

    # Sjekk om noen piksler innenfor fargeområdet er detektert
        return cv2.countNonZero(mask) > 0

    def apply_gamma_correction(self, frame, gamma=1.6):
        """Apply gamma correction to adjust brightness."""
        inv_gamma = 1.0 / gamma
        table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
        return cv2.LUT(frame, table)

# Set up the camera with Picam
picam2 = Picamera2()
picam2.preview_configuration.main.size = (960, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Initialize YOLO ball detection
yolo_detector = YoloBallDetection("bestNEW_ncnn_model")

# Start FPS timer
prev_time = time.time()

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Apply Gamma Correction
    frame = yolo_detector.apply_gamma_correction(frame, gamma=1.5)

    # Detect balls
    results = yolo_detector.detect_ball(frame)

    # Annotate the frame using YOLO's built-in method and color filtering
    annotated_frame = yolo_detector.annotate_ball(frame, results)

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Display FPS on the frame
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)

    # Exit the program if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Close all windows
cv2.destroyAllWindows()
