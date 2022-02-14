import sys
import time
from sys import exit
from random import random
from gpiozero import CamJamKitRobot
from gpiozero import LineSensor

robot = CamJamKitRobot()

#####################

# Linjedetektor
pinLineFollower = 25

sensor = LineSensor(pinLineFollower)

def lineseen():
    print("line seen")

def linenotseen():
    print("line not seen")


sensor.when_line = lineseen
sensor.when_no_line = linenotseen
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    exit()

