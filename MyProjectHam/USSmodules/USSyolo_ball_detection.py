import cv2
import numpy as np
from ultralytics import YOLO

class YoloBallDetection:
    def __init__(self, model_path, mtx, dist, newcameramtx, roi):
        self.model = YOLO(model_path)
        self.target_classes = {"Blue_ball": 1, "Green_ball": 2, "Red_ball": 0}
        self.mtx = mtx
        self.dist = dist
        if len(self.dist.shape) > 1:
            self.dist = self.dist.flatten()
        self.newcameramtx = newcameramtx
        self.roi = roi
        self.rvecs = []  # Rotasjonsvektorer (hent fra kalibreringsdata)
        self.tvecs = []  # Translasjonsvektorer (hent fra kalibreringsdata)

    def undistort_frame(self, frame):
        undistorted = cv2.undistort(frame, self.mtx, self.dist, None, self.newcameramtx)
        x, y, w, h = self.roi
        return undistorted[y:y+h, x:x+w]

    def detect_ball(self, frame):
        results = self.model(frame)
        return results

    def get_object_position(self, x, y):
        """
        Beregner objektets posisjon i verdenskoordinater basert på bildekoordinater.
        """
        try:
            # Fjern forvrengning fra bildepunktet
            undistorted_point = cv2.undistortPoints(
                np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2),
                cameraMatrix=self.mtx,
                distCoeffs=self.dist
            )

            # Legg til en homogen koordinat (z=1) for 3D-transformasjon
            undistorted_point = np.append(undistorted_point[0][0], 1.0).reshape(3, 1)

            # Konverter rotasjonsvektor til rotasjonsmatrise
            rvec = np.asarray(self.rvecs[0], dtype=np.float32).reshape((3, 1))
            tvec = np.asarray(self.tvecs[0], dtype=np.float32).reshape((3, 1))
            R, _ = cv2.Rodrigues(rvec)

            # Invers rotasjonsmatrise
            R_inv = np.linalg.inv(R)

            # Omregn til verdenskoordinater
            camera_point = R_inv @ (undistorted_point - tvec)
            world_point = camera_point.flatten()

            # Debugging: Skriv ut verdier for validering
            print(f"Undistorted point: {undistorted_point}")
            print(f"R: {R}")
            print(f"R_inv: {R_inv}")
            print(f"Camera point: {camera_point}")
            print(f"World point: {world_point}")

            return world_point

        except cv2.error as e:
            raise RuntimeError(f"OpenCV Error in get_object_position: {e}")
        except Exception as e:
            raise RuntimeError(f"General Error in get_object_position: {e}")


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

    def annotate_and_get_position(self, frame, results):
        """
        Annotate detected balls on the frame using YOLO's built-in method and apply color filtering.
        """
        # Sjekk om frame er gyldig
        if frame is None or frame.size == 0:
            raise ValueError("Invalid frame received from the camera.")
        
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

                # Calculate world coordinates based on image coordinates
                world_coords = self.get_object_position(x_center, y_center)

                print(f"Detected |{class_name}| at image coordinates ({x_center}, {y_center}) "
                      f"and world coordinates {world_coords}")

                # Add text to the image with world coordinates
                cv2.putText(annotated_frame, f"{class_name}: World {world_coords}",
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        return annotated_frame

    def apply_gamma_correction(self, frame, gamma=1.6):
        inv_gamma = 1.0 / gamma
        table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
        return cv2.LUT(frame, table)
