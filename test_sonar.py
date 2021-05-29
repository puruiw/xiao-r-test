import os
import time
import RPi.GPIO as GPIO

ECHO = 4
TRIG = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def busy_wait(delay):
    start = time.time()
    while time.time() - start < delay:
        pass
    return


def get_distance():
    GPIO.output(TRIG, GPIO.LOW)
    busy_wait(0.01)
    GPIO.output(TRIG, GPIO.HIGH)
    busy_wait(0.000010)
    GPIO.output(TRIG, GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    t1 = time.time()
    while GPIO.input(ECHO):
        pass
    t2 = time.time()
    busy_wait(0.01)
    return (t2 - t1) * 340 / 2


while True:
    try:
        distance = get_distance()
        print(f'Distance = {distance}m')
        busy_wait(1)
    except KeyboardInterrupt:
        break
print('Clean up.')
GPIO.cleanup()
