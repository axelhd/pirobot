import time
from gpiozero import DistanceSensor

pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

print("Measuring Distance To Object In Front")

try:
    while True:
        print("Distance To Object In Front: %1.f cm" % sensor.distance * 100)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting")