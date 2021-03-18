#!/usr/bin/env python3

from datetime import datetime
import RPi.GPIO as GPIO

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 200000
RECEIVE_PIN = 23

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    print ("**Started packet capture...**")

    cumulative_time = 0
    beginning_time = datetime.now()

    while True:
        if GPIO.input(RECEIVE_PIN) ==


        while True:
            print (datetime.now())
            sleep(0.5)
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.microseconds
    print ("**Ended recording**")
    print (len(RECEIVED_SIGNAL[0]), 'samples recorded')
    GPIO.cleanup()
