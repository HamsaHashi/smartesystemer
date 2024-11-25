
from USSmodules.USSyolo_ball_detection import YoloBallDetection
from USSmodules.USScamera_setup import setup_camera
from USSconfig.UUScalibration import load_calibration_data
import cv2
import time
import os

# Laste inn calibrasjons data
calibration_data = load_calibration_data()

mtx, dist, newcameramtx, roi, rvecs, tvecs = calibration_data
model_path = "/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/USSresources/USSmodel/SokHam_ncnn_model"
yolo_detector = YoloBallDetection(model_path, mtx, dist, newcameramtx, roi)

# Initialiser rvecs og tvecs i YoloBallDetection for for å få verdensposisjon
yolo_detector.rvecs = rvecs
yolo_detector.tvecs = tvecs

picam2 = setup_camera()
prev_time = time.time()

while True:
    frame = picam2.capture_array()
    frame = yolo_detector.apply_gamma_correction(frame, gamma=1.5)
    results = yolo_detector.detect_ball(frame)
    annotated_frame = yolo_detector.annotate_and_get_position(frame, results)

    # FPS utregning
    current_time = time.time()
    fps = 1 / max((current_time - prev_time), 1e-6)
    prev_time = current_time

    # Viser FPS på live cam
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("H-Camera", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
