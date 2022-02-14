import sys
from pynput_robocorp.keyboard import Key, Listener
from gpiozero import CamJamKitRobot

print("Initializing robot...")
robot = CamJamKitRobot()
print("Robot ready!")

MotorSpeedLeft = 0.45
MotorSpeedRight = 0.3

MotorForward = (MotorSpeedLeft, MotorSpeedRight)
MotorBackward = (-MotorSpeedLeft, -MotorSpeedRight)
MotorLeft = (MotorSpeedLeft, -MotorSpeedRight)
MotorRight = (-MotorSpeedLeft, MotorSpeedRight)


def on_release(key):
    print("on_release: {}".format(key))
    robot.stop()


def move(key):
    print("move: {}".format(key))

    if key.char == "w":
        robot.value = MotorForward
        return

    if key.char == "a":
        robot.value = MotorLeft
        return

    if key.char == "s":
        robot.value = MotorBackward
        return

    if key.char == "d":
        robot.value = MotorRight
        return

    if key.char == "e":
        robot.stop()
        return

    if key.char == "q":
        robot.stop()
        print("Quitting...")
        sys.exit()


with Listener(on_press=move, on_release=on_release) as listener:
    print("Ready for your command...")
    listener.join()
