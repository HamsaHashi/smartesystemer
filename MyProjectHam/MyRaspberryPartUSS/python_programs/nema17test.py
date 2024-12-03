import RPi.GPIO as GPIO
import time

# GPIO-pinner for steppermotorene
MOTORS = {
   "front_left": {"STEP": 4, "DIR": 14},
  "front_right": {"STEP": 17, "DIR": 18},
   "back_left": {"STEP": 22, "DIR": 23},
    "back_right": {"STEP": 9, "DIR": 25},
}
#MOTORS = {
    #"front_left": {"STEP": 4, "DIR": 14},
    #"front_right": {"STEP": 17, "DIR": 18},
    #"back_left": {"STEP": 16, "DIR": 15}
    #"back_right": {"STEP": 9, "DIR": 25},
#}
# Forsinkelse mellom steg (hastighet)
DELAY = 0.001  # Mindre forsinkelse = raskere bevegelse
DURATION = 30  # Varighet i sekunder for frem- og tilbakekjøring


# Sett opp GPIO
GPIO.setmode(GPIO.BCM)
for motor in MOTORS.values():

    
    GPIO.setup(motor["STEP"], GPIO.OUT)
    GPIO.setup(motor["DIR"], GPIO.OUT)

def move_all_motors(direction, duration):
    """
    Beveger alle motorene samtidig i en bestemt retning i et gitt antall sekunder.
    """
    #retningen for alle motorene
    for motor in MOTORS.values():
        GPIO.output(motor["DIR"], GPIO.HIGH if direction == "forward" else GPIO.LOW)
    
    # Beveg motorene i den angitte tiden
    end_time = time.time() + duration
    while time.time() < end_time:
        for motor in MOTORS.values():
            GPIO.output(motor["STEP"], GPIO.HIGH)
        time.sleep(DELAY)
        for motor in MOTORS.values():
            GPIO.output(motor["STEP"], GPIO.LOW)
        time.sleep(DELAY)

try:
    print("Kjører alle motorer rett frem i 20 sekunder...")
    move_all_motors("forward", DURATION)

    time.sleep(1)  # Kort pause mellom frem- og tilbakekjøring

    print("Kjører alle motorer tilbake i 20 sekunder...")
    #move_all_motors("backward", DURATION)

except KeyboardInterrupt:
    print("Test avbrutt!")

finally:
    GPIO.cleanup()
    print("GPIO-pinner nullstilt.")
