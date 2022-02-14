import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

motorspeed = 0.3

motorforward = (motorspeed, motorspeed)
motorbackward = (-motorspeed, -motorspeed)
motorleft = (motorspeed, 0)
motorright = (0, motorspeed)

robot.value = motorforward
time.sleep(1)

robot.value = motorbackward
time.sleep(1)

robot.value = motorleft
time.sleep(1)

robot.value = motorright
time.sleep(1)

robot.stop()