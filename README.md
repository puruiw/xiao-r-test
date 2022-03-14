# Experiments
## Random Walk
Run from the robot as root:
```
source venv/bin/activate
python -m demo.random_move
```

## ROS keyboard control.
From host:
```
push_to_xiaor.sh
start_ros_host.sh <host ip>
```
From robot:
```
start_ros_robot.sh <host ip>
```
Now there should be a window showing live from the robot camera. From host, start keyboard controller by:
```
source /opt/ros/noetic/setup.bash
start_keyboard_controller.sh <host ip>
```
