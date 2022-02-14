import sys
import time
from sys import exit
from random import random
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

def move_random(robot):
    if random() > 0.5:
        robot.right()
    else:
        robot.left()
    time.sleep(random())
    robot.stop()


robot.backward()
time.sleep(0.5)
move_random(robot)
robot.forward()
time.sleep(2)
robot.stop()

exit()


for i in range(4):
    print(i)
    robot.forward()
    time.sleep(1.3)
    move(robot)


print("Nu stopper vi")
robot.stop()
print("slut")
