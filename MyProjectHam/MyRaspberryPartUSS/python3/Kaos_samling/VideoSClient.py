""" # VideoSClient.py
I denne koden setter jeg opp et PiCamera2-kamera for å fange video med en oppløsning på 640x480
piksler og RGB888-format. Deretter oppretter jeg en TCP-socket for å koble til Windows-maskinen
min via IP-adressen '192.168.1.145' på port 8000. Inne i en løkke fanger jeg kontinuerlig videoframene
fra kameraet, sender lengden på hvert bilde etterfulgt av bildedataene i en binær strøm. Koden sørger
for å tømme bufferet for å sikre at dataene sendes raskt til klienten. Til slutt, når strømmen avsluttes,
lukker jeg tilkoblingen ordentlig for å frigjøre ressursene. Denne versjonen inkluderer feilhåndtering
for å håndtere eventuelle nettverksfeil og gjenopprette forbindelsen hvis den brytes.
"""

import io
import socket
import struct
import time
from picamera2 import Picamera2

# Funksjon for å sende data med feilhåndtering
def send_data(connection, frame):
    try:
        # Logg bildelengde for feilsøking
        frame_length = len(frame)
        print(f"Sender bilde med lengde: {frame_length} bytes")

        # Send lengden på bildet
        connection.write(struct.pack('<L', len(frame)))  # little-endian byte rekkefølge ->(minste,større...++)
        connection.flush()  # Sikrer sending av data til Windows for streaming
        
        # Send bildet
        connection.write(frame.tobytes())
    except (ConnectionResetError, BrokenPipeError) as e:
        print(f"Feil under sending: {e}")
        return False  # Indiker at sendingen feilet
    return True  # Indiker at sendingen var vellykket

# Oppsettet av kameraet
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.start()

# Koble til Windows-maskinen
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # forteller at jeg bruker en IP4-adresse, communikasjon med 32bits addy
client_socket.settimeout(20)  # Legger til en timeout for forbindelsen

try:
    client_socket.connect(('192.168.1.145', 8000))  # Bruk IP-adressen til Windows-maskinen
    connection = client_socket.makefile('wb')

    while True:
        try:
            # Fanger et bilde fra kameraet
            frame = picam2.capture_array()
            
            # Forsøk å sende data, gjenopprett hvis det feiler
            if not send_data(connection, frame):
                print("Forsøker å gjenopprette tilkobling...")
                client_socket.close()
                time.sleep(2)  # Vent litt før du forsøker på nytt
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(('192.168.1.145', 8000))
                connection = client_socket.makefile('wb')
                continue  # Gå til neste iterasjon for å sende data på nytt

        except Exception as e:
            print(f"Generell feil under sending: {e}")
            break

finally:
    print("Avslutter tilkobling...")
    try:
        # Signaliserer slutten av strømmen ved å sende en lengde på 0
        connection.write(struct.pack('<L', 0))
        connection.close()
        client_socket.close()
    except Exception as e:
        print(f"Feil ved lukking av tilkobling: {e}")
