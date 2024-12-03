import cv2
from ultralytics import YOLO


model = YOLO('XXXXXXXXXXXXXXXXXX.pt')  # Endrer denne stien til vår modell .pt senere
camera = cv2.VideoCapture(0) 

if not camera.isOpened():
    print("Kameraet kunne ikke åpnes")
    exit()

# Minimum sikkerhet (50%)
MIN_CONFIDENCE = 0.5


while True:
    
    ret, frame = camera.read()

    if not ret:
        print("Kunne ikke lese fra kameraet")
        break

    
    results = model(frame)

    
    detected_objects = results[0].boxes  
    
    # Sjekker om detekterte objekter er fra de spesifikke klassene (rød: 0, blå: 1, grønn: 2)
    ball_classes = [0, 1, 2]  # Klasser for røde, blå og grønne baller
    ball_detected = False

    filtered_boxes = []
    for box in detected_objects:
        class_id = int(box.cls)
        confidence = box.conf  # Få konfidensen for detected objektet
        
        # Sjekk om detektert objekt tilhører ballklassene og har minimum 50% konfidens
        if class_id in ball_classes and confidence >= MIN_CONFIDENCE:
            filtered_boxes.append(box)
            ball_detected = True

    if ball_detected:
        print("Ball detektert med over 50% sikkerhet: True")
    else:
        print("Ingen ball detektert med over 50% sikkerhet: False")

    # Annoter bildet med detekterte baller hvis noen er funnet
    if filtered_boxes:  # annoterer hvis baller er funnet
        annotated_frame = results[0].plot()
        cv2.imshow("Detektering av baller", annotated_frame)
    else:
        cv2.imshow("Ingen baller funnet", frame) 

    # 'q' for å avslutte
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
