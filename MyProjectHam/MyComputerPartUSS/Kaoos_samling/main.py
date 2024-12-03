import cv2
# Samler klasser fra Video_S_Mottaker.py og Real_Ball_Detection_Yolov8.py i en klasse
from Kaoos_samling.Video_S_Mottaker import VideoSMottaker
from Kaoos_samling.Real_Ball_Detection_Yolov8 import YoloBallDetection

# Setter opp Yolov8 modellen min
model_path = model_path = r"C:\MyComputerPartUSS\best.pt"
Real_Ball_Detection = YoloBallDetection(model_path)

# Setter opp video mottakeren (windows vet hvem som sender video og mottar video fra Raspberry Pi)
Video_S_Mottaker = VideoSMottaker(host = '192.168.1.145', port = 8000)

try:
    while True:
        # Motta video fra Raspberry Pi
        frame = Video_S_Mottaker.Motta_Frame()
        if frame is None:
            print("main.py: Ingen bilde mottatt, forsøker igjen...")
            continue # prøver igjen hvis det ikke gikk
        

         # Kjører ball deteksjonen og får tilbake en annotert frame
        annotated_frame = Real_Ball_Detection.Detect_Ball(frame)

         # Viser det annoterte bildet
        cv2.imshow("Annotert bilde", annotated_frame)

        # finner x og y koordinatene for hver ball basert på detekterte baller!!!!!!!!!!!!!!
        x, y = Real_Ball_Detection.Get_Ball_Coordinates(annotated_frame)
        print("Ballens x og y koordinater: ", x, y)  
        
         # Trykk 'q' for å avslutte
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

except Exception as e:
    print("main.py: ", f"Feil ved video mottakelse: {e}")


finally:
    Video_S_Mottaker.close()
    cv2.destroyAllWindows()
