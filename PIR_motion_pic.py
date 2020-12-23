from gpiozero import MotionSensor
from picamera import PiCamer
import time
import datetime

pir=MotionSensor(4)
//gpio 4 or pin 7

cam=PiCamera()

def getFileName():
return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%s.jpg")

while True:
filename=getFileName()
pir.wait_for_motion

print("Motion Detected!")

cam.start_preview()
came.capture(filename)
cam.stop_preview()

time.sleep(5)