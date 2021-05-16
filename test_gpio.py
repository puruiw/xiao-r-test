import time

import RPi.GPIO as GPIO

mode = GPIO.getmode()
print(mode)
GPIO.setmode(GPIO.BCM)

LED0 = 10
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
for i in range(20):
    GPIO.output(LED0, i % 2)
    time.sleep(0.5)

GPIO.cleanup()
