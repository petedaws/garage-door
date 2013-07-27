#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,False)


TCP_IP = '192.168.1.4'
TCP_PORT = 8080 
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr # change this to a log statement
while 1:
    data = conn.recv(BUFFER_SIZE)
    if data is None: break
    if data == 'open':
    	print 'Received DOOR Activation from %s' % str(addr) # change this to a log statement
	conn.sendall('Received Correct DOOR Activation Code from %s\n' % str(addr))
	GPIO.output(7,True)
	time.sleep(4)
	GPIO.output(7,False)
    else: 
    	print 'Incorrect DOOR Activation password received from %s' % str(addr)
	try:	
		conn.sendall('Incorrect DOOR Activation password received from %s\n' % str(addr))
	except Exception as e:
		conn.close()	
		conn, addr = s.accept()	
		print e
conn.close()
