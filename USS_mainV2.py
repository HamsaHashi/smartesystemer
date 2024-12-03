from USSmodules.USSyolo_ball_detection import YoloBallDetection
from USSmodules.USScamera_setup import setup_camera
from USSconfig.UUScalibration import load_calibration_data
from USSmodules.USSmotor_control import MecanumDrive
from ultrasonics import Ultrasonics  # Legg til ultrasonics-modulen
import cv2
import time 

# Laste inn kalibreringsdata
calibration_data = load_calibration_data()
mtx, dist, newcameramtx, roi, rvecs, tvecs = calibration_data

model_path = "/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/USSresources/USSmodel/SokHam_ncnn_model"
yolo_detector = YoloBallDetection(model_path, mtx, dist, newcameramtx, roi)

# Initialiser rvecs og tvecs i YoloBallDetection for å få verdensposisjon
yolo_detector.rvecs = rvecs
yolo_detector.tvecs = tvecs

picam2 = setup_camera()

# Initialiser motorstyring
motor_pins = [
    (4, 14),  # Motor 1 (front-left)
    (17, 18),  # Motor 2 (front-right)
    (22, 23),  # Motor 3 (back-left)
    (9, 25)   # Motor 4 (back-right)
]
robot = MecanumDrive(motor_pins)

# Initialiser ultralydsensor
TRIG_PIN = 23
ECHO_PIN = 24
MIN_DISTANCE = 15  # cm, minimum avstand før roboten reagerer
ultrasonics = Ultrasonics(TRIG_PIN, ECHO_PIN)

# Initialiser variabler for FPS-utregning
prev_time = time.time()

try:
    while True:
        # Mål avstand til hindringer
        distance = ultrasonics.check_distance()
        print(f"Avstand: {distance} cm")

        if distance <= MIN_DISTANCE:
            # Hindring oppdaget
            print("Hindring oppdaget! Stopper og rygger.")
            robot.stop()
            time.sleep(0.5)
            robot.move(0, -1, 0)  # Rygg
            time.sleep(0.5)
            robot.stop()
            continue

        # Hvis ingen hindringer, detekter ball
        frame = picam2.capture_array()
        frame = yolo_detector.apply_gamma_correction(frame, gamma=1.5)
        results = yolo_detector.detect_ball(frame)
        annotated_frame = yolo_detector.annotate_and_get_position(frame, results)

        for box in results[0].boxes:
            # Finn verdenskoordinater for ballen
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            x_center = (x1 + x2) // 2
            y_center = (y1 + y2) // 2
            world_coords = yolo_detector.get_object_position(x_center, y_center)

            # Beregn bevegelsesvektorer basert på verdenskoordinater
            vx = world_coords[0] * 0.01
            vy = world_coords[1] * 0.01
            omega = 0  # Juster rotasjon ved behov

            # Flytt roboten mot ballen
            robot.move(vx, vy, omega, step_delay=0.002)

        # FPS-utregning
        current_time = time.time()
        fps = 1 / max((current_time - prev_time), 1e-6)
        prev_time = current_time

        # Viser FPS på live cam
        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("H-Camera", annotated_frame)

        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    print("Programmet ble avbrutt.")
finally:
    robot.stop()
    robot.cleanup()
    ultrasonics.cleanup()
    cv2.destroyAllWindows()
