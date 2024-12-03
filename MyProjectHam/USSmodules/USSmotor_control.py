# Denne filen håndterer styringen av steppermotorene koblet til de omnidireksjonelle hjulene.

import RPi.GPIO as GPIO
import time

class MecanumDrive:
    def __init__(self, motor_pins):
        """
        Initialiserer motorene og GPIO-pinnene.
        motor_pins: Liste med fire motorer, hver med (DIR, STEP) pinner.
        """
        self.motor_pins = motor_pins
        GPIO.setmode(GPIO.BCM)
        for dir_pin, step_pin in motor_pins:
            GPIO.setup(dir_pin, GPIO.OUT)
            GPIO.setup(step_pin, GPIO.OUT)
    
    def move(self, vx, vy, omega, step_delay=0.002):
        """
        Beregner motorhastighet og beveger roboten basert på ønsket bevegelse.
        vx: Hastighet i x-retning.
        vy: Hastighet i y-retning.
        omega: Rotasjonshastighet.
        step_delay: Forsinkelse mellom trinn for stabilitet.
        """
        # Matrise for mekanumhjul
        motor_speeds = [
            vy + vx + omega,  # Motor 1 (front-left)
            vy - vx - omega,  # Motor 2 (front-right)
            vy - vx + omega,  # Motor 3 (back-left)
            vy + vx - omega   # Motor 4 (back-right)
        ]

        # Normaliser hastighetene
        max_speed = max(abs(speed) for speed in motor_speeds)
        if max_speed > 1.0:
            motor_speeds = [speed / max_speed for speed in motor_speeds]

        # Beregn antall trinn for hver motor
        step_counts = [int(abs(speed) * 200) for speed in motor_speeds]

        # Beveg motorene
        for step in range(max(step_counts)):
            for i, (dir_pin, step_pin) in enumerate(self.motor_pins):
                if step < step_counts[i]:
                    GPIO.output(dir_pin, GPIO.HIGH if motor_speeds[i] > 0 else GPIO.LOW)
                    GPIO.output(step_pin, GPIO.HIGH)
                    time.sleep(step_delay)
                    GPIO.output(step_pin, GPIO.LOW)
    
    def stop(self):
        """
        Stopper alle motorer.
        """
        for dir_pin, step_pin in self.motor_pins:
            GPIO.output(step_pin, GPIO.LOW)

    def cleanup(self):
        """
        Rydder opp GPIO-pinnene.
        """
        GPIO.cleanup()
