import time

from smbus import SMBus

XIAOR_I2C_ADDR = 0x17

smbus = SMBus(1)
time.sleep(1)

# !!! Not working
# Code presents in XiaoR's modified SMBus lib, but no functioning example.
# Not used in their official client.
def get_servo_angle(servo):
    return smbus.read_byte_data(XIAOR_I2C_ADDR, servo)


def set_servo_angle(servo, angle):
    smbus.write_byte_data(XIAOR_I2C_ADDR, 255, servo)
    smbus.write_byte_data(XIAOR_I2C_ADDR, angle, 255)


set_servo_angle(1, 0)
time.sleep(1)
#print(get_servo_angle(1))

set_servo_angle(2, 0)
for i in range(0, 90):
    set_servo_angle(2, i)
    time.sleep(0.5)
