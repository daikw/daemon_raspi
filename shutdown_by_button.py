#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)

# GPIO26 : shutdown button
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def shutdown(channel):
    os.system("sudo shutdown -h now")


GPIO.add_event_detect(26, GPIO.FALLING, callback = shutdown, bouncetime = 2000)

while True:
    time.sleep(100)
