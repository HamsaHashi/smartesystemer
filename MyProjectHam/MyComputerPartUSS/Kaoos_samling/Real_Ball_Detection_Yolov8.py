import cv2
import numpy as np
from ultralytics import YOLO

class YoloBallDetection:

    # Angir sti til min custom trente YOLO modell
    def __init__(self, model_path):
        self.model = YOLO(r"C:\MyComputerPartUSS\best.pt")

    # Bruker modellen til å detektere baller
    def Detect_Ball(self, frame):
        results = self.model(frame)
        return results
    
    # detektere baller og annotere bildene med bounding box og angi klassenavn
    def Annotate_Ball(self, frame, results):
        for box in results[0].boxes:
            class_id = int(box.cls)
            confidence = box.conf
            x1, y1, x2, y2 = map(int, box.xyxy[0]) # bounding box koordinater
            class_name = results[0].names[class_id] # klassenavn

            # Annoterer bildet med bounding box og klassenavn kun conf over 0.65
            if confidence >= 0.6:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name} {confidence: .2f}" , (x1, y1 - 10),
                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        return frame
    
    # en funksjon for å bestemme hvilken ball jeg ønsker x og y koordinatene til
    def get_ball(self, results, class_id):
        for box in results[0].boxes:
            if class_id == int(box.cls):
                x1, y1, x2, y2 = box.xyxy[0]  
                x_sentrum = (x1 + x2) / 2
                y_sentrum = (y1 + y2) / 2
                hight = y2 - y1
                width = x2 -x1
                return x_sentrum, y_sentrum, width, hight



    # Henter x og y koordinatene til sentrum av detektert ball
    def Get_Ball_Coordinates(self, results):
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0] #  
            x_sentrum = (x1 + x2) / 2
            y_sentrum = (y1 + y2) / 2
            return x_sentrum, y_sentrum