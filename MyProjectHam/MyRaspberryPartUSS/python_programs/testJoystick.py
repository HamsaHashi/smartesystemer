import pygame
import time 

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    pygame.event.pump()
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    print(f"x={x_axis}, y={y_axis}")
    time.sleep(0.05)