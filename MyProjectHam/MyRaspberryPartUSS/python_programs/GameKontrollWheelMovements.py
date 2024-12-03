import pygame
import RPi.GPIO as GPIO
import time
import threading

# Motorpinner konfigurert
MOTORS = {
    "front_left": {"STEP": 4, "DIR": 14},
    "front_right": {"STEP": 17, "DIR": 18},
    "back_left": {"STEP": 22, "DIR": 23},
    "back_right": {"STEP": 9, "DIR": 25},
}

# GPIO-oppsett
GPIO.setmode(GPIO.BCM)
for motor, pins in MOTORS.items():
    GPIO.setup(pins["STEP"], GPIO.OUT)
    GPIO.setup(pins["DIR"], GPIO.OUT)

# Globale variabler for bevegelseskontroll
motor_speeds = {motor: 0 for motor in MOTORS}  # Hastighet for hver motor (-1 til 1)
motor_directions = {motor: "forward" for motor in MOTORS}  # Retning for hver motor
running = True  # Kontroll for trådene

# Funksjon for å kontrollere en motor
def motor_control(motor, step_pin, dir_pin):
    global motor_speeds, motor_directions, running
    while running:
        speed = motor_speeds[motor]
        if speed != 0:
            GPIO.output(dir_pin, GPIO.HIGH if motor_directions[motor] == "forward" else GPIO.LOW)
            delay = max(0.002, 0.002 / abs(speed))  # Juster hastigheten
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(delay)
        else:
            time.sleep(0.01)  # Pause når motoren er inaktiv

# Start tråder for motorstyring
threads = []
for motor, pins in MOTORS.items():
    t = threading.Thread(target=motor_control, args=(motor, pins["STEP"], pins["DIR"]))
    t.start()
    threads.append(t)

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

try:
    while True:
        pygame.event.pump()

        # Hent joystick-akser
        forward_back_axis = apply_deadzone(joystick.get_axis(1))
        left_right_axis = apply_deadzone(joystick.get_axis(0))

        # Oppdater motorhastigheter og retning
        for motor in MOTORS.keys():
            if forward_back_axis > 0:
                motor_speeds[motor] = forward_back_axis
                motor_directions[motor] = "backward"
            elif forward_back_axis < 0:
                motor_speeds[motor] = -forward_back_axis
                motor_directions[motor] = "forward"
            elif left_right_axis > 0:  # Roter høyre
                if motor in ["front_left", "back_left"]:
                    motor_speeds[motor] = left_right_axis
                    motor_directions[motor] = "backward"
                else:
                    motor_speeds[motor] = left_right_axis
                    motor_directions[motor] = "forward"
            elif left_right_axis < 0:  # Roter venstre
                if motor in ["front_left", "back_left"]:
                    motor_speeds[motor] = -left_right_axis
                    motor_directions[motor] = "forward"
                else:
                    motor_speeds[motor] = -left_right_axis
                    motor_directions[motor] = "backward"
            else:
                motor_speeds[motor] = 0  # Stopp motoren

        time.sleep(0.01)  # Kort pause for å avlaste CPU-en

except KeyboardInterrupt:
    print("Avslutter programmet...")
finally:
    # Rydder opp GPIO-pinnene
    running = False  # Stopp trådene
    for t in threads:
        t.join()
    GPIO.cleanup()
