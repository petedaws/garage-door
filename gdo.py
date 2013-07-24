#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,False)


TCP_IP = '192.168.1.4'
TCP_PORT = 8080 
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if data is None: break
    if data == 'open':
	GPIO.output(7,True)
	time.sleep(2)
	GPIO.output(7,False)
conn.close()
