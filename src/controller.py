#encoding=utf8
import sys
import time
from sys import exit
from random import random
from gpiozero import CamJamKitRobot

print("Starter op...")


robot = CamJamKitRobot()

#####################
import pynput

from pynput.keyboard import Key, Listener

run_delay = 0.1

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    try:
        if key.char=="w":
            print("FREMAD")
            forward()
        elif key.char=="a":
            left()
        elif key.char=="d":
            print("Højre")
            right()
        elif key.char=="s":
            print("Bak")
            backward()
        else:
            print("STOP")
            robot.stop()
    except AttributeError:
        print("Unknown key")
        robot.stop()

def on_release(key):
    if key == Key.esc:
        print("Afslutter")
        robot.stop()
        sys.exit()
        return False


def backward(t=run_delay):
    robot.backward()
def forward(t=run_delay):
    robot.forward()
def left(t=run_delay):
    print("Venstre")
    robot.left()
def right(t=run_delay):
    robot.right()

with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Klar")
    listener.join()



sys.exit()



while True:
    kommando = raw_input()
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
