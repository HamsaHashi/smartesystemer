#!/usr/bin/env python3

import serial
import time
####	Alt her kjører en gang

# Åpne serial kommunikasjon:
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
# Sove i 3 sekunder slik at arduino får tid til å starte slik at vi unngår error når den ikke oppnår communication med en gang
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")


####	Til her (for kommunikasjon til Arduino ->).
try:
    while True:
        # Legger til sleep så while ikke tar alle ressurser til CPU så alt blir veldig slow. 
        time.sleep(0.01)
        
# Denne er for å sende communication til arduino
        # En if som sjekker om nr av bites er større enn 0 for motatt data fra arduino til raspberry.
        if ser.in_waiting > 0:
            # Arduino kommuniserer i bites oversetter derfor fra bytes til string i readline()
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print("Serial Kommunikasjon Avsluttet")
    ser.close()