#!/usr/bin/env python

# from flask import Flask
# server = Flask(__name__)
# 
# @server.route("/")
# def hello():
#      return "Hello World!"
# 
# if __name__ == "__main__":
#      server.run(host='0.0.0.0')


import threading
import serial
import time

connected = False
port = '/dev/ttyUSB0'
baud = 115200

serial_port = serial.Serial(port, baud, timeout=0)

def handle_data(data):
    print(data)

def read_from_port(ser):
     while not connected:
          global connected
          #serin = ser.read()
          connected = True

          while True:
               print("test")
               reading = ser.readline().decode()
               handle_data(reading)
               time.sleep(0.5)


thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()