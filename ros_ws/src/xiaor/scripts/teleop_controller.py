#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist

from my_robot.xiao_r_robot import XiaoRRobot
from my_robot.timer import busy_wait

class Controller:
    def __init__(self):
        self._robot = XiaoRRobot()
        self._robot.init()
    
    def __call__(self, twist:Twist):
        rospy.logdebug(f"{rospy.get_caller_id()}: got {twist}")
        if twist.linear.x > 0:
            self._robot.start_forward()
        elif twist.linear.x < 0:
            self._robot.start_backward()
        elif twist.angular.z > 0:
            self._robot.start_turn_left()
        elif twist.angular.z < 0:
            self._robot.start_turn_right()
        else:
            self._robot.stop()


def listener():
    rospy.init_node('xiaor_teleop_controller')
    controller = Controller()
    rospy.Subscriber("xiaor_command", Twist, controller)
    rospy.spin()


if __name__ == '__main__':
    listener()