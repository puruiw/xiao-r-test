import random
import time

from my_robot.xiao_r_robot import XiaoRRobot

def random_move():

  r = XiaoRRobot()
  r.init()
 
  while True:
    try:
      r.start_forward(0.7)
      while True:
        distance = r.sonar.get_distance()
        print(distance)
        if distance < 0.5:
          break
        time.sleep(0.01)
      r.stop()
      r.start_turn_left(0.3)
      time.sleep(random.random() * 0.5 + 0.1)
    except KeyboardInterrupt:
      r.cleanup()
      return


if __name__ == r'__main__':
  random_move()