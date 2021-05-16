import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ENA = 13
IN1 = 19
IN2 = 16

try:
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(ENA, 1)
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)

    time.sleep(3)

    GPIO.output(ENA, 0)
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
