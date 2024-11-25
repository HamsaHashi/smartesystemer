import socket
import struct
import numpy as np
import cv2

class VideoSMottaker:
    #  Setter opp en server socket og venter på en klient som kobler seg til
    def __init__(self, host = '192.168.1.145', port = 8000):
        print("Video_S_Mottaker.py: ", "Setter opp server socket...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        print("Video_S_Mottaker.py: ", f"Serveren er bundet til {host}:{port}")
        self.server_socket.listen(0)
        print("Video_S_Mottaker.py: ", "Venter på klient tilkobling...")
        self.connection, self.client_address = self.server_socket.accept()
        print("Video_S_Mottaker.py: ", f"Tilkoblet til klient: {self.client_address}")
        self.connection = self.connection.makefile('rb') # Readbinary

    #  Sjekker om jeg har mottatt en frame og hvis jeg har det så leser jeg den
    def Motta_Frame(self):
        try:
            image_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                print("Video_S_Mottaker.py: ", "Ingen bildelengde mottatt, avslutter...")
                return None
            
            image_stream = self.connection.read(image_len)
            image = np.frombuffer(image_stream, dtype=np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            return image
        except Exception as e:
            print("Video_S_Mottaker.py: ", f"Feil ved mottakelse av frame: {e}")
            return None
        
    
    #  Lukker serveren og tilkoblingen hvis jeg er ferdig med å motta rammer
    def close(self):
        print("Video_S_Mottaker.py: ", "Lukker alle tilkoblinger og serveren...")
        self.connection.close()
        self.server_socket.close()
        print("Video_S_Mottaker.py: ", "Tilkoblingen er lukket.")
