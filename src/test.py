import time
#import cv2
from gpiozero import CamJamKitRobot
#from gpiozero import DistanceSensor
from pynput.keyboard import Key, Listener


#webcam = cv2.VideoCapture(0)

robot = CamJamKitRobot()

MotorSpeedLeft = 0.45
MotorSpeedRight = 0.3

MotorForward = (MotorSpeedLeft, MotorSpeedRight)
MotorBackward = (-MotorSpeedLeft, -MotorSpeedRight)
MotorLeft = (MotorSpeedLeft, -MotorSpeedRight)
MotorRight = (0, MotorSpeedRight)

#pinTrigger = 17
#pinEcho = 18

def move(key):
    if key == Key.w:
        robot.value = MotorForward

    if key == Key.a:
        robot.value = MotorLeft

    if key == Key.s:
        robot.value = MotorBackward

    if key == Key.d:
        robot.value = MotorRight

    if key == Key.e:
        robot.stop()

#sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

while True:
    #stream_ok, frame = webcam.read()

    #if stream_ok:
        #cv2.imshow('Webcam', frame)
    #robot.value = MotorForward
    DistanceToObjectInFront = sensor.distance * 100


    def move(key):
        if key == Key.w:
            robot.value = MotorForward

        if key == Key.a:
            robot.value = MotorLeft

        if key == Key.s:
            robot.value = MotorBackward

        if key == Key.d:
            robot.value = MotorRight

        if key == Key.e:
            robot.stop()


    def on_release(key):
        robot.stop()

    with Listener(on_press=move, on_release=on_release) as listener:
        lis cv
 #b
if
 prtener.join()
   # if cv2.waitKey(1) & 0xFF == 27:
        #break
    #elif DistanceToObjectInFront <= 35:
        print("To Close")
        robot.stop()
        robot.value = MotorBackward
        time.sleep(1)
        robot.stop()
        robot.value = MotorLeft
        time.sleep(3)
        robot.value = MotorForward
    #else:
       #print(DistanceToObjectInFront)
        #time.sleep(0.5)

#cv2.destroyAllWindows()

#webcam.release()
