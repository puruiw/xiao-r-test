import time

import RPi.GPIO as GPIO

mode = GPIO.getmode()
print(mode)
GPIO.setmode(GPIO.BCM)

LED0 = 10
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
pwm = GPIO.PWM(LED0, 1000)
pwm.start(0)

for i in range(500):
    pwm.ChangeDutyCycle(i % 100)
    time.sleep(0.05)

GPIO.cleanup()
