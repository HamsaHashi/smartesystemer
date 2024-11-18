import pygame
from pygame.locals import *

# Initialiser pygame joystick
pygame.init()
pygame.joystick.init()

# Koble til den første kontrolleren
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Using joystick: {joystick.get_name()}")

# Testloop for å fange input
while True:
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")
