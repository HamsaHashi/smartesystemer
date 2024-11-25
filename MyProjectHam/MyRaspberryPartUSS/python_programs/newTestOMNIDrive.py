import pygame
import serial
import time
import math

# Konfigurer seriell kommunikasjon
arduino = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
arduino.dtr = False  # Deaktiver automatisk reset
time.sleep(1)        # Vent til Arduino er klar
arduino.dtr = True   # Aktiver kommunikasjon
time.sleep(2)
print("Starter kommunikasjon med Arduino...")

# Konfigurer joystick
pygame.init()
pygame.event.set_allowed(None)  # Deaktiver andre hendelser for raskere respons
pygame.event.set_allowed(pygame.JOYAXISMOTION)  # Kun oppdater joystick-hendelser
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Funksjoner for justering av joystick-input
def apply_deadzone(value, threshold=0.1):
    """Fjern små variasjoner fra joystick-input."""
    if abs(value) < threshold:
        return 0
    return round(value, 2)

def calculate_direction_and_speed(x_axis, y_axis, max_speed=500, min_speed=500):
    """Beregn retning og hastighet fra joystick-input."""
    speed = math.sqrt(x_axis**2 + y_axis**2)  # Magnitude
    if speed > 1:  # Normaliser hvis verdien er utenfor [-1, 1]
        speed = 1
    angle = math.atan2(y_axis, x_axis) * 180 / math.pi  # Vinkel i grader
    adjusted_speed = max(int(speed * max_speed), min_speed)  # Minimumshastighet
    return angle, adjusted_speed

def brake(current_speed, current_angle, steps=10, delay=0.05):
    """Reduser hastigheten gradvis mot null."""
    for i in range(steps, 0, -1):
        reduced_speed = int(current_speed * (i / steps))
        command = f'V{int(current_angle)}S{reduced_speed}'  # Behold retningen med redusert hastighet
        arduino.write((command + '\n').encode())
        print(f"DEBUG: Bremser med kommando: {command}")
        time.sleep(delay)
    print("DEBUG: Bremsing fullført. Sender stoppkommando.")
    arduino.write(b'S\n')  # Send stoppkommando etter bremsing

# Variabel for å holde styr på siste kommando og timeout
last_command = None
last_sent_time = time.time()  # Tidsstempel for siste kommando sendt
joystick_in_deadzone = False  # Sporer om joystick er i dødsonen

while True:
    pygame.event.pump()

    # Hent joystick-akser (sideveis og frem/tilbake)
    x_axis = apply_deadzone(joystick.get_axis(0))  # Sideveis joystick-verdi
    y_axis = apply_deadzone(-joystick.get_axis(1))  # Frem/tilbake joystick-verdi

    # Beregn retning og hastighet
    if x_axis != 0 or y_axis != 0:
        joystick_in_deadzone = False  # Ikke i dødsonen lenger
        angle, speed = calculate_direction_and_speed(x_axis, y_axis)
        current_command = f'V{int(angle)}S{speed}'  # Send vinkel og hastighet
    else:
        # Joystick er i dødsonen
        if not joystick_in_deadzone:  # Bare brems hvis vi nettopp gikk inn i dødsonen
            joystick_in_deadzone = True  # Merk at vi er i dødsonen
            if last_command and 'S' not in last_command:
                # Hvis en bevegelseskommando var aktiv, brems før stopp
                last_angle = float(last_command.split('V')[1].split('S')[0])  # Hent forrige vinkel
                last_speed = int(last_command.split('S')[1])  # Hent forrige hastighet
                brake(last_speed, last_angle)  # Utfør bremsing
            current_command = 'S'
        else:
            current_command = None  # Ingen ny kommando

    # Unngå å sende for mange stoppkommandoer
    current_time = time.time()
    if current_command == 'S' and current_time - last_sent_time < 0.1:
        print("Ignorerer gjentatt stoppkommando.")
        current_command = None

    # Send kommando
    if current_command and (current_command != last_command or current_time - last_sent_time > 0.1):  # Timeout på 100 ms
        print(f"Sender kommando: {current_command}")  # DEBUGGING
        arduino.write((current_command + '\n').encode())  # Send kommando til Arduino
        print(f"Kommando sendt: {current_command}")  # Bekreft etter sending
        last_command = current_command
        last_sent_time = current_time
    else:
        if current_command:
            print(f"Kommando ikke sendt: {current_command}")  # Hvis kommando ignoreres

    # Kort pause for å unngå overbelastning
    time.sleep(0.005)
