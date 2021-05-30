import time
import threading

import RPi.GPIO as GPIO

from my_robot import config
from my_robot.timer import busy_wait


SOUND_SPEED = 340


class Sonar(object):
  def __init__(self, trig_pin, echo_pin, measure_interval=config.SONAR_MEASURE_INTERVAL, max_distance=3.0) -> None:
      super().__init__()
      self.trig_pin = trig_pin
      self.echo_pin = echo_pin
      self.measure_interval = measure_interval
      self._max_distance = max_distance

      self.value = float('inf')

      self.lock = threading.Lock()
      self.thread = None
      self.quit = False
  
  def init(self):
    GPIO.setup(self.trig_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(self.echo_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    self.thread = threading.Thread(target=self._measure_thread)
    self.thread.start()

  def cleanup(self):
    if self.thread:
      self.quit = True
      self.thread.join(timeout=config.CLEANUP_WAIT)

  def max_distance(self):
    return self._max_distance

  def get_distance(self):
    with self.lock:
      return self.value

  def _measure(self):
    GPIO.output(self.trig_pin, GPIO.LOW)
    busy_wait(0.01)
    GPIO.output(self.trig_pin, GPIO.HIGH)
    busy_wait(0.000010)
    GPIO.output(self.trig_pin, GPIO.LOW)
    while not GPIO.input(self.echo_pin):
        pass
    t1 = time.time()
    while GPIO.input(self.echo_pin):
        pass
    t2 = time.time()
    busy_wait(0.01)

    new_value = value = (t2 - t1) * SOUND_SPEED / 2
    with self.lock:
      self.value = new_value
  
  def _measure_thread(self):
    while not self.quit:
      self._measure()
      time.sleep(self.measure_interval)
    
