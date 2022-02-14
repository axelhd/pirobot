import sys
import time
from sys import exit
from random import random
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

#####################


robot.forward()
time.sleep(1)

robot.backward()
time.sleep(1)


robot.left()
time.sleep(0.5)

robot.right()
time.sleep(0.5)

robot.stop()

exit()

