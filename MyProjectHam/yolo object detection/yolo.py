import cv2
import numpy as np
from picamera2 import Picamera2
from ultralytics import YOLO
import time


# Konverter yolo modell til ncnn format sti:
model_path = "/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/YOLO Object Detection/SokHam_ncnn_model"

# Laster inn calibration data fra .npz filen
calibration_data = np.load('/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/yolo object detection/Calibration_Raspi_Cam/calibration112_data.npz')
mtx = calibration_data['cameraMatrix']
dist = calibration_data['dist']
rvecs = calibration_data['rvecs']  # Rotasjonsvektorer
tvecs = calibration_data['tvecs']  # Translasjonsvektorer

# Generer newcameramtx og ROI
frame_width, frame_height = 960, 720  
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (frame_width, frame_height), 1, (frame_width, frame_height))

# Definerer en klasse for YOLO ball deteksjon
class YoloBallDetection:
    def __init__(self, model_path, mtx, dist, newcameramtx, roi):
        self.model = YOLO(model_path)
        self.target_classes = {"Blue_ball": 1, "Green_ball": 2, "Red_ball": 0}  
        self.mtx = mtx
        self.dist = dist
        self.newcameramtx = newcameramtx
        self.roi = roi
        self.rvecs = rvecs
        self.tvecs = tvecs

    # Definerer metoder for bildebehandling
    def undistort_frame(self, frame):
        # legger til undistort_frame metoden som input i bilde.
        undistorted = cv2.undistort(frame, self.mtx, self.dist, None, self.newcameramtx)
        x, y, w, h = self.roi
        return undistorted[y:y+h, x:x+w]

    # Definerer metoder for ball deteksjon
    def detect_ball(self, frame):
        # Detect balls using the YOLO model.
        results = self.model(frame)
        return results

     # Beregner objektets posisjon i verdenskoordinater
    def get_object_position(self, x, y):
        # Objektets 2D-punkt i bildet
        image_point = np.array([[x, y]], dtype=np.float32)
        # Beregner objektets posisjon i 3D
        world_point, _ = cv2.projectPoints(image_point, self.rvecs[0], self.tvecs[0], self.mtx, self.dist)
        return world_point.flatten()

    # Annoterer baller og beregner posisjon
    def annotate_and_get_position(self, frame, results):
        """Annotate detected balls on the frame using YOLO's built-in method and apply color filtering."""
        annotated_frame = results[0].plot()  # Use built-in method to draw bounding boxes and labels
        
        # Iterate through detections to apply color filtering
        for box in results[0].boxes:
            confidence = box.conf[0]
            class_id = int(box.cls[0])

            # Check if the detection is one of the target classes and has sufficient confidence
            if confidence >= 0.64 and class_id in self.target_classes.values():
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract coordinates as integers
                x_center = (x1 + x2) // 2
                y_center = (y1 + y2) // 2
                class_name = results[0].names[class_id]
                roi = frame[y1:y2, x1:x2]  # Region of Interest (ROI)
                
                # Perform color filtering to confirm the object
                if not self.color_filter(roi, class_name):
                    continue  # Skip this detection if color filtering fails

               

                # Beregn verdenskoordinater basert på bildekoordinater
                world_coords = self.get_world_coordinates(x_center, y_center)

                print(f"Detected |{class_name}| at image coordinates ({x_center}, {y_center}) "
                      f"and world coordinates {world_coords}")

                # Legg til tekst på bildet med verdenskoordinater
                cv2.putText(annotated_frame, f"{class_name}: World {world_coords}",
                           (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        return annotated_frame

    # Definerer metoder for fargefiltrering
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

    # Definerer metoder for gamma korreksjon for å justere lysstyrken
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
yolo_detector = YoloBallDetection(model_path, mtx, dist, newcameramtx, roi)

# Start FPS timer
prev_time = time.time()

# Nå starter hovedløkken for å fange og behandle bilder fra kameraet.
while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Apply Gamma Correction
    frame = yolo_detector.apply_gamma_correction(frame, gamma=1.5)

    # Detect balls
    results = yolo_detector.detect_ball(frame)

    # Annotate the frame using YOLO's built-in method and color filtering
    annotated_frame = yolo_detector.annotate_and_get_position(frame, results)

    # Calculate FPS
    current_time = time.time()
    fps = 1 / max((current_time - prev_time), 1e-6)
    prev_time = current_time

    # Display FPS on the frame
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow("H-Camera", annotated_frame)

    # Exit the program if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Close all windows
cv2.destroyAllWindows()
