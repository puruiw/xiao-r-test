import random
import time

from my_robot.xiao_r_robot import XiaoRRobot


def move_till_hit(robot: XiaoRRobot, max_time_s):
  """Run for max_time_s or until sonar detects something within 0.5m."""
  start = time.time()
  robot.start_forward(0.7)
  while time.time() < start + max_time_s:
    distance = robot.sonar.get_distance()
    print(distance)
    if distance < 0.5:
      break
    time.sleep(0.01)
  robot.stop()


def random_move():
  r = XiaoRRobot()
  r.init()
 
  while True:
    try:
      move_till_hit(r, 2.0)
      if random.random() < 0.5:
        r.start_turn_left(1.0)
      else:
        r.start_turn_right(1.0)
      time.sleep(random.random() * 0.5 + 0.1)
    except KeyboardInterrupt:
      r.cleanup()
      return


if __name__ == r'__main__':
  random_move()