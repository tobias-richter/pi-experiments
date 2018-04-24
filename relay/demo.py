#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO-Pins - Edit!!!

pinList = [17, 27, 22, 10, 9, 5, 6, 13]

# Loop through Pins

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

SleepTimeL = 0.2

# Loop

try:
    while True:

        for i in pinList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(SleepTimeL);
            GPIO.output(i, GPIO.HIGH)

        pinList.reverse()

        for i in pinList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(SleepTimeL);
            GPIO.output(i, GPIO.HIGH)

        pinList.reverse()

# End
except KeyboardInterrupt:
    print "  Ende"

    GPIO.cleanup()