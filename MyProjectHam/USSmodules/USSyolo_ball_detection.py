import cv2
import numpy as np
from ultralytics import YOLO

class YoloBallDetection:
    def __init__(self, model_path, mtx, dist, newcameramtx, roi):
        self.model = YOLO(model_path)
        self.target_classes = {"Blue_ball": 1, "Green_ball": 2, "Red_ball": 0}
        self.mtx = mtx
        self.dist = dist
        self.newcameramtx = newcameramtx
        self.roi = roi

    def undistort_frame(self, frame):
        undistorted = cv2.undistort(frame, self.mtx, self.dist, None, self.newcameramtx)
        x, y, w, h = self.roi
        return undistorted[y:y+h, x:x+w]

    def detect_ball(self, frame):
        results = self.model(frame)
        return results

    def annotate_and_get_position(self, frame, results):
    #Annotate detected balls on the frame using YOLO's built-in method and apply color filtering."""
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
