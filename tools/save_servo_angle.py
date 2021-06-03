"""Save an default angle for each servo.

USE WITH CAUTION!!

During bootup, the controller chip will set all servos to their default angles.
We need to make sure these angles are reachable from ANY pose. We do not include
this function in the default lib.
"""

import time
import sys

import RPi.GPIO as GPIO
from smbus import SMBus

from my_robot import xiao_r_robot as xr


def set_angle(smbus, servo_id, angle):
  smbus.write_byte_data(xr.SERVO_I2C_ADDR, 255, servo_id)
  smbus.write_byte_data(xr.SERVO_I2C_ADDR, angle, 255)


def save_angle(smbus):
  smbus.write_byte_data(xr.SERVO_I2C_ADDR, 255, 17)
  smbus.write_byte_data(xr.SERVO_I2C_ADDR, 1, 255)


def set_all(angles):
  smbus = SMBus(xr.SERVO_SM_BUS)
  for i, angle in enumerate(angles):
    set_angle(smbus, i + 1, angle)
    time.sleep(1.0)
  save_angle(smbus)


if __name__ == r'__main__':
  set_all([0, 80])