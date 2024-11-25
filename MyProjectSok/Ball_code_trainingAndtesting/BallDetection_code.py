import cv2
from ultralytics import YOLO
import numpy as np
import tensorflow as tf

class BallDetection:
    def __init__(self):
        
        self.model = YOLO('yolov8n.pt')  
       
        self.tensorflow_model = self.load_tensorflow_model()

    def load_tensorflow_model(self):
       
        model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False)
        return model

    def is_spherical(self, contour):
       
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
        return 0.7 < circularity < 1.3  # Circularity er nær 1 aka "spherical"

    def check_diameter(self, bounding_rect):
        # Calculate the diameter of the object from the bounding box width
        diameter = bounding_rect[2]  
        return abs(diameter - 62) <= 5  

    def detect_color(self, frame, bounding_rect):
        # Extract the region of interest (ROI) der ballene er lokalisert 
        x, y, w, h = bounding_rect
        roi = frame[y:y + h, x:x + w]
        
        # komputere the average fargen in the ROI
        avg_color_per_row = cv2.mean(roi)
        b, g, r, _ = avg_color_per_row

        # Detect ball color
        if r > 150 and g < 100 and b < 100:
            return "red"
        elif r > 150 and g > 150 and b < 100:
            return "blue"
        elif g > 150 and r < 100 and b < 100:
            return "green"
        else:
            return "unknown"

    def process_frame(self, frame):
        # YOLO object detection
        results = self.model(frame)
        
        for result in results:
            for box in result.boxes:
               
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                bounding_rect = (x1, y1, x2 - x1, y2 - y1)
                
                
                if self.is_spherical(result.masks):  
                    
                    if self.check_diameter(bounding_rect):
                        color = self.detect_color(frame, bounding_rect)
                        
                        if color == "red":
                            print("Red ball detected")
                        elif color == "blue":
                            print("Blue ball detected")
                        elif color == "green":
                            print("Green ball detected")
                        else:
                            print("Unknown color detected")
                    else:
                        print("Ball does not have the correct diameter")
                else:
                    print("Object is not spherical")
                    
    def start_camera(self):
       
        cap = cv2.VideoCapture(0)  
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            self.process_frame(frame)
            
            cv2.imshow('Ball Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()


ball_detector = BallDetection()
ball_detector.start_camera()
