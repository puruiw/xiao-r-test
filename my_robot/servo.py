import RPi.GPIO as GPIO


class Servo(object):
  def __init__(self, smbus, i2c_addr, servo_id) -> None:
    super().__init__()
    self.smbus = smbus
    self.i2c_addr = i2c_addr
    self.servo_id = servo_id
    self.angle_target = None

  def init(self):
    pass

  def cleanup(self):
    pass

  def set_angle(self, angle):
    self.angle_target = angle
    self.smbus.write_byte_data(self.i2c_addr, 255, self.servo_id)
    self.smbus.write_byte_data(self.i2c_addr, angle, 255)
    