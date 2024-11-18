#!/usr/bin/env python3

import serial
import time


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")


try:
    while True: 
        time.sleep(0.5)
        print("send melding til Arduinoo");
        ser.write("Hei fra Raspberry Pi\n".encode('utf-8'))
except KeyboardInterrupt:
    print("Serial Kommunikasjon Avsluttet")
    ser.close()
