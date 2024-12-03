import cv2
from ultralytics import YOLO
import threading
import time

class ObjectDetector:
    def __init__(self, model_path, frame_grabber, skip_frames=5):
        self.model = YOLO(model_path)
        self.frame_grabber = frame_grabber
        self.skip_frames = skip_frames
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self.run_detection, daemon=True).start()

    def run_detection(self):
        frame_count = 0
        while self.running:
            frame = self.frame_grabber.get_frame()
            if frame is None:
                continue
            
            # Skip frames to reduce processing load
            frame_count += 1
            if frame_count % self.skip_frames != 0:
                continue

            # Perform object detection
            results = self.model(frame)
            self.annotate_and_display(frame, results)

    def annotate_and_display(self, frame, results):
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                confidence = box.conf[0]
                class_id = int(box.cls[0])

                # Only display detections with confidence > 75%
                if confidence > 0.75:
                    label = f"{self.model.names[class_id]} {confidence:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Real-Time Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

    def stop(self):
        self.running = False
        cv2.destroyAllWindows()
 