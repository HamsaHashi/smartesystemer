import cv2
from ultralytics import YOLO
from time import sleep
from picamera2 import Picamera2
import time
 
# Denne funksjonen returnerer pixel koordinat på detected object
def get_ball(results, class_id):
        for box in results[0].boxes:
            if class_id == int(box.cls):
                x1, y1, x2, y2 = box.xyxy[0]  
                x_sentrum = (x1 + x2) / 2
                y_sentrum = (y1 + y2) / 2
                hight = y2 - y1
                width = x2 -x1
                return x_sentrum, y_sentrum, width, hight
            print(f"X: {x_sentrum}, Y: {y_sentrum}n\
                  w: {width}, h: {hight}")
            

# Set up the camera with Picam
picam2 = Picamera2()
picam2.preview_configuration.main.size=(640,480)
picam2.preview_configuration.main.format= "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
time.sleep(3)


model = YOLO("SokHam_ncnn_model")  # Stien til best.pt-file
# Minimum sikkerhet (50%) 
MIN_CONFIDENCE = 0.7

# Funksjon for å vise resultater i sanntid
while True:

    frame = picam2.capture_array()
    
    # Kjør deteksjon med YOLOv8-modellen
    results = model(frame)

    # Få resultatene fra YOLO og filtrer kun ball-detektering
    detected_objects = results[0].boxes  # YOLOv8 gir tilbake boksene (detekterte objekter)
    

    # Get inteference time
    interference_time = results[0].speed['inference']
    fps = 1000 / interference_time
    text = f'FPS: {fps:.2f}'

    # Definere front og posisjon
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = detected_objects.shape[1] - text_size[0] - 10  # 10 pixels from the right
    text_y = text_size[1] + 10  # 10 pixels from the top

    # Tegn teksten på det annoterte frame
    cv2.putText(detected_objects, text, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA) 
    # Sjekk om detekterte objekter er fra de spesifikke klassene (rød: 0, blå: 1, grønn: 2)
    ball_classes = [0, 1, 2]  # Klasser for røde, blå og grønne baller
    ball_detected = False  # Initialiser bolsk signal

    filtered_boxes = []
    for box in detected_objects:
        class_id = int(box.cls)
        confidence = box.conf  # Få konfidensen for dette objektet
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        class_name = results[0].names[class_id]

        
        # Sjekk om detektert objekt tilhører ballklassene og har minimum 50% konfidens
        if class_id in ball_classes and confidence >= MIN_CONFIDENCE:
            filtered_boxes.append(box)
            ball_detected = True  # Sett bolsk signal til True

    # Print bolsk signal for ball detektering
    if ball_detected:
        riktig = get_ball(results, 0)
        print(f"Ball detektert med over 50% sikkerhet: True \n {riktig}")
    else:
        print("Ingen ball detektert med over 50% sikkerhet: False")

    # Annoter bildet med detekterte baller hvis noen er funnet
    if filtered_boxes:  # Kun annoter hvis baller er funnet
        annotated_frame = results[0].plot()
     # Vis alltid med samme vindu
        detections= 0
        display_frame = annotated_frame if detections else frame
        cv2.imshow("Live Feed", display_frame)


    # Trykk 'q' for å avslutte
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Slipp kameraet og lukk alle vinduer

picam2.stop()
cv2.destroyAllWindows()