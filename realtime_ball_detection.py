import cv2
from ultralytics import YOLO

# Last inn din YOLOv8-modell (endre sti til din .pt-modell)
model = YOLO('XXXXXXXXXXXXXXXXXX.pt')  # Endre denne stien til din .pt-fil

# velger rasp kameraet
camera = cv2.VideoCapture(0)  # 0 er standardkameraet

if not camera.isOpened():
    print("Kameraet kunne ikke åpnes")
    exit()

# Minimum sikkerhet (50%)
MIN_CONFIDENCE = 0.5

# Funksjon for å vise resultater i sanntid
while True:
    # Les fra kameraet
    ret, frame = camera.read()

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Slipp kameraet og lukk alle vinduer
camera.release()
cv2.destroyAllWindows()
