#!/usr/bin/env python3

from datetime import datetime
from time import sleep
import time


if __name__ == '__main__':
    while True:
        print (time.time_ns())
        sleep(0.5)
        print (time.time_ns())