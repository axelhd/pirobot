import sys
import time
from random import random
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

def move(robot):
    if random() > 0.5:
        robot.right()
    else:
        robot.left()
    time.sleep(random())
    robot.stop()


for i in range(4):
    print(i)
    robot.forward()
    time.sleep(1.3)
    move(robot)


print("Nu stopper vi")
robot.stop()
print("slut")
