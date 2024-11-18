import serial
import time
import keyboard

# Koble til den serielle porten (sjekk hvilken port Arduino bruker)
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Endre til riktig port
time.sleep(2)  # Gi tid til Arduino å starte opp

try:
    while True:
        if keyboard.is_pressed('up'):  # Pil opp for fremover
            arduino.write(b'F\n')  # Send fremover
            print("Kjører fremover...")
        elif keyboard.is_pressed('down'):  # Pil ned for bakover
            arduino.write(b'B\n')  # Send bakover
            print("Kjører bakover...")
        elif keyboard.is_pressed('left'):  # Pil venstre for venstre sving
            arduino.write(b'L\n')  # Send venstre
            print("Svinger venstre...")
        elif keyboard.is_pressed('right'):  # Pil høyre for høyre sving
            arduino.write(b'R\n')  # Send høyre
            print("Svinger høyre...")
        else:
            arduino.write(b'S\n')  # Stopp hvis ingen taster er trykket
            print("Stoppet...")
            time.sleep(0.1)  # Pause for å unngå for mange signaler

except KeyboardInterrupt:
    print("Programmet stoppes.")
finally:
    arduino.close()  # Lukk den serielle forbindelsen når programmet avsluttes
