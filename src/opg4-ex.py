import sys
import time
from sys import exit
from random import random
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

#####################


while True:
    print("Giv mig en kommando: ", )
    kommando = input()
    kommando=kommando.strip()
    print("Kommandoen var", kommando)
    if kommando == "x":
        print("Afslutter")
        robot.stop()
        exit()
    if kommando == "r":
        robot.right()
        time.sleep(0.5)
        robot.stop()

    if kommando == "l":
        robot.left()
        time.sleep(0.5)
        robot.stop()

    if kommando == "f":
        robot.forward()
        time.sleep(0.5)
        robot.stop()

    if kommando == "b":
        robot.backward()
        time.sleep(0.5)
        robot.stop()


robot.stop()
exit()
