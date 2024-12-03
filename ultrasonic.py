import RPi.GPIO as GPIO
import time

class Ultrasonics:
    def __init__(self, trig_pin, echo_pin, max_distance=200):
        """
        Initialiserer ultralydsensor.
        trig_pin: GPIO-pin for trig.
        echo_pin: GPIO-pin for echo.
        max_distance: Maksimal avstand i cm.
        """
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.max_distance = max_distance
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def check_distance(self):
        """
        Mål avstand med ultralydsensor.
        """
        GPIO.output(self.trig_pin, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, GPIO.LOW)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2  # Beregn avstanden i cm

        # Begrens avstanden til maks
        if distance > self.max_distance:
            return self.max_distance
        return distance

    def cleanup(self):
        """
        Rydder opp GPIO-pinnene.
        """
        GPIO.cleanup()
