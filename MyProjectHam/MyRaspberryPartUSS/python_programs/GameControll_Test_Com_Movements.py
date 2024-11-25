import pygame
import serial
import time

# Konfigurer seriell kommunikasjon
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)
print("Starter kommunikasjon med Arduino...")

# Konfigurer joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Funksjoner for justering av joystick-input
def apply_deadzone(value, threshold=0.2):
    """Fjern små variasjoner fra joystick-input."""
    if abs(value) < threshold:
        return 0
    return value

def adjust_speed(value, max_speed=800):
    """Skaler joystick-verdi til ønsket hastighet."""
    return int(value * max_speed)

# Variabel for å holde styr på siste kommando
last_command = None

while True:
    pygame.event.pump()

    # Hent joystick-akser
    forward_back_axis = apply_deadzone(joystick.get_axis(1))
    print(f"Joystick-akseverdi (frem/tilbake): {forward_back_axis}")  # DEBUGGING

    # Kalkuler kommando basert på joystick-bevegelse
    if abs(forward_back_axis) > 0.1:
        if forward_back_axis < 0:
            current_command = f'F{adjust_speed(-forward_back_axis)}'
        else:
            current_command = f'B{adjust_speed(forward_back_axis)}'
    else:
        current_command = 'S'  # Stop-kommando

    # Send kommando kun hvis den er forskjellig fra forrige
    if current_command != last_command:
        arduino.write((current_command + '\n').encode())
        print(f"Sendt kommando: {current_command}")  # DEBUGGING
        last_command = current_command

    # Håndter rotasjonsknapper
    if joystick.get_button(3):  # Venstre knapp
        current_command = 'L360'  # Roter 360 grader til venstre
        if current_command != last_command:
            arduino.write((current_command + '\n').encode())
            print(f"Sendt kommando: {current_command}")
            last_command = current_command
    elif joystick.get_button(1):  # Høyre knapp
        current_command = 'R360'  # Roter 360 grader til høyre
        if current_command != last_command:
            arduino.write((current_command + '\n').encode())
            print(f"Sendt kommando: {current_command}")
            last_command = current_command

    # Kort pause for å unngå overbelastning
    time.sleep(0.01)
