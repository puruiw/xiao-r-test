import RPi.GPIO as GPIO

from my_robot import config


class Motor(object):
  def __init__(self, en_pin, in1_pin, in2_pin) -> None:
    super().__init__()
    self.en_pin = en_pin
    self.in1_pin = in1_pin
    self.in2_pin = in2_pin
    self.pwm = None

  def init(self):
    GPIO.setup(self.en_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.in1_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.in2_pin, GPIO.OUT, initial=GPIO.LOW)
    self.pwm = GPIO.PWM(self.en_pin, config.PWM_FREQUENCE)

  def cleanup(self):
    pass

  def start_forward(self, power=1.0):
    self.pwm.start(power * 100)
    self._set_io(1, 0, 1)

  def start_backward(self, power=1.0):
    self.pwm.start(power * 100)
    self._set_io(1, 1, 0)

  def stop(self):
    self.pwm.stop()
    self._set_io(0, 0, 0)

  def _set_io(self, en, in1, in2):
    GPIO.output(self.en_pin, en)
    GPIO.output(self.in1_pin, in1)
    GPIO.output(self.in2_pin, in2)