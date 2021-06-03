import RPi.GPIO as GPIO
from smbus import SMBus

from my_robot import config, motor, servo, sonar

SONAR_TRIG_PIN = 17
SONAR_ECHO_PIN = 4

MOTOR_L_EN = 20
MOTOR_L_IN1 = 21
MOTOR_L_IN2 = 26

MOTOR_R_EN = 13
MOTOR_R_IN1 = 19
MOTOR_R_IN2 = 16

SERVO_SM_BUS = 1
SERVO_I2C_ADDR = 0x17

CAMERA_PITCH_SERVO_ID = 1
CAMERA_YAW_SERVO_ID = 2


class XiaoRRobot(object):
  def __init__(self) -> None:
      super().__init__()
      self.smbus = SMBus(SERVO_SM_BUS)
      self.sonar = sonar.Sonar(SONAR_TRIG_PIN, SONAR_ECHO_PIN, config.SONAR_MEASURE_INTERVAL)
      self.motor_l = motor.Motor(MOTOR_L_EN, MOTOR_L_IN1, MOTOR_L_IN2)
      self.motor_r = motor.Motor(MOTOR_R_EN, MOTOR_R_IN1, MOTOR_R_IN2)

      self.camera_pitch_servo = servo.Servo(self.smbus, SERVO_I2C_ADDR, CAMERA_PITCH_SERVO_ID)
      self.camera_yaw_servo = servo.Servo(self.smbus, SERVO_I2C_ADDR, CAMERA_YAW_SERVO_ID)

      self.components = [self.sonar, self.motor_l, self.motor_r, self.camera_pitch_servo, self.camera_yaw_servo]

  def init(self):
    GPIO.setmode(GPIO.BCM)
    for c in self.components:
      c.init()
    self.camera_pitch_servo.set_angle(0)
    self.camera_yaw_servo.set_angle(80)
  
  def cleanup(self):
    for c in self.components:
      c.cleanup()
    GPIO.cleanup()

  def start_forward(self, power=1.0):
    self.motor_l.start_forward(power)
    self.motor_r.start_forward(power)

  def start_backward(self, power=1.0):
    self.motor_l.start_backward(power)
    self.motor_r.start_backward(power)

  def start_turn_left(self, power=1.0):
    self.motor_l.start_backward(power)
    self.motor_r.start_forward(power)

  def start_turn_right(self, power=1.0):
    self.motor_l.start_forward(power)
    self.motor_r.start_backward(power)

  def stop(self):
    self.motor_l.stop()
    self.motor_r.stop()

