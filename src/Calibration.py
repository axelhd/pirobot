import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

robot = CamJamKitRobot()

MotorSpeedLeft = 0.45
MotorSpeedRight = 0.3

MotorForward = (MotorSpeedLeft, MotorSpeedRight)
MotorBackward = (-MotorSpeedLeft, -MotorSpeedRight)
MotorLeft = (MotorSpeedLeft, -MotorSpeedRight)
MotorRight = (0, MotorSpeedRight)

pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)


while True:
    robot.value = MotorForward
    DistanceToObjectInFront = sensor.distance * 100
    if DistanceToObjectInFront <=35:
        print("To Close")
        robot.stop()
        robot.value = MotorBackward
        time.sleep(1)
        robot.stop()
        robot.value = MotorLeft
        time.sleep(3)
        robot.value = MotorForward
    else:
        print(DistanceToObjectInFront)
        time.sleep(0.5)