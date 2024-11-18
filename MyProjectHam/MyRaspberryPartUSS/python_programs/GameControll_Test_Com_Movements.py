import pygame
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 250000, timeout=1)
time.sleep(2)

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

def apply_deadzone(value, threshold=0.1):
    if abs(value) < threshold:
        return 0
    return value

def adjust_speed(value, max_speed=800):
    return int(value * max_speed)

while True:
    pygame.event.pump()

    forward_back_axis = apply_deadzone(joystick.get_axis(1))
    
    if abs(forward_back_axis) > 0.1:
        if forward_back_axis < 0:
            arduino.write(f'F{adjust_speed(-forward_back_axis)}\n'.encode())
        elif forward_back_axis > 0:
            arduino.write(f'B{adjust_speed(forward_back_axis)}\n'.encode())
    else:
        arduino.write(b'S\n')

    if joystick.get_button(3):
        arduino.write(b'L360\n')
        print("Roterer 360 grader til venstre")
    elif joystick.get_button(1):
        arduino.write(b'R360\n')
        print("Roterer 360 grader til høyre")

    time.sleep(0.01)
