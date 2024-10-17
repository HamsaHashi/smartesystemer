import cv2
from ultralytics import YOLO
from time import sleep

from picamera2 import Picamera2, Preview 
#from picamera import PiCamera
import time

#camera = PiCamera2() #
picam2 = Picamera2()


picam2_config = picam2.create_preview_configuration()
picam2.configure(picam2_config)

picam2.start_preview(Preview.QTGL) #picam2
picam2.start() #picam2

time.sleep(2)

picam2.capture_file("test_photo.jpg")

# Last inn din YOLOv8-modell (endre sti til din .pt-modell)
model = YOLO('/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/best.pt')  # Stien til best.pt-fil


# velger rasp kameraet
picam2 = cv2.VideoCapture(1)  # 0 er standardkameraet

if not picam2.isOpened():
    print("Kameraet kunne ikke åpnes")
    exit()

# Minimum sikkerhet (50%) 
MIN_CONFIDENCE = 0.5

# Funksjon for å vise resultater i sanntid
while True:
    # Les fra kameraet
    ret, frame = picam2.read()

    if not ret:
        print("Kunne ikke lese fra kameraet")
        break

    # Kjør deteksjon med YOLOv8-modellen
    results = model(frame)

    # Få resultatene fra YOLO og filtrer kun ball-detektering
    detected_objects = results[0].boxes  # YOLOv8 gir tilbake boksene (detekterte objekter)
    
    # Sjekk om detekterte objekter er fra de spesifikke klassene (rød: 0, blå: 1, grønn: 2)
    ball_classes = [0, 1, 2]  # Klasser for røde, blå og grønne baller
    ball_detected = False  # Initialiser bolsk signal

    filtered_boxes = []
    for box in detected_objects:
        class_id = int(box.cls)
        confidence = box.conf  # Få konfidensen for dette objektet
        
        # Sjekk om detektert objekt tilhører ballklassene og har minimum 50% konfidens
        if class_id in ball_classes and confidence >= MIN_CONFIDENCE:
            filtered_boxes.append(box)
            ball_detected = True  # Sett bolsk signal til True

    # Print bolsk signal for ball detektering
    if ball_detected:
        print("Ball detektert med over 50% sikkerhet: True")
    else:
        print("Ingen ball detektert med over 50% sikkerhet: False")

    # Annoter bildet med detekterte baller hvis noen er funnet
    if filtered_boxes:  # Kun annoter hvis baller er funnet
        annotated_frame = results[0].plot()
        cv2.imshow("Detektering av baller", annotated_frame)
    else:
        cv2.imshow("Ingen baller funnet", frame)  # Vis live feed uten annotering

    # Trykk 'q' for å avslutte
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Slipp kameraet og lukk alle vinduer
picam2.release()
cv2.destroyAllWindows()

