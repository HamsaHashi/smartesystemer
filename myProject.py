import tkinter as tk
from tkinter import Button
import cv2
from ultralytics import YOLO

#       INNEHOLD AV DETTE KODEN:
    # Linje 14 -> Den ferdigtrente modellen som gjenkjenner hva vi ser på bilde.
    # Linje 17, 18, 19 -> De variablene for knappene i gui vinduet for pause osv.
    # Linje 22 -> De funksjonene som starter video streamen
    # Linje 29 -> Oppdaterer  
    # Linje  ->

# YOLO-modellen
model = YOLO('yolov8n.pt')

# Global variabel for å kontrollere om kameraet er på pause eller ikke
paused = False
cap = None
running = False  # Variabel for å stoppe kameraet

# Funksjon for å starte kameraet
def start_cam():
    global paused, cap, running
    if not running:
        running = True
        cap = cv2.VideoCapture(0)  # Webkamera
        update_frame()

# Funksjon for å oppdatere rammen fra kameraet
def update_frame():
    global paused, cap, running
    if running:
        if not paused:
            ret, frame = cap.read()
            if ret:
                # YOLO-inference på den nåværende rammen
                results = model(frame)
                result_frame = results[0].plot()

                # Vis resultatene i OpenCV-vinduet
                cv2.imshow('YOLO Objekt gjenkjenning', result_frame)

        # Vent på "q" eller oppdater vinduet i løpet av 1 millisekund
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_cam()

        # Planlegg neste ramme i GUI-løkken
        window.after(10, update_frame)

# Funksjon for å pause kameraet
def pause_cam():
    global paused
    paused = not paused  # Bytt mellom pause og start

# Funksjon for å avslutte programmet
def stop_cam():
    global cap, running
    running = False
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()

# Opprett Tkinter-vinduet

window = tk.Tk()
window.title("Webcam Control")

# Opprett knapper
start_button = Button(window, text="Start Cam", command=start_cam)
start_button.pack()

pause_button = Button(window, text="Pause/Resume Cam", command=pause_cam)
pause_button.pack()

stop_button = Button(window, text="Stop Cam", command=stop_cam)
stop_button.pack()

# Start GUI-løkken
window.mainloop()
