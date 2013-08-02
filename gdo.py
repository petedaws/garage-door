#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	GPIO.output(7,False)
except Exception as e:
	print e, 'Failed to setup GPIO'
	exit(0)


if len(sys.argv) > 1:
	if sys.argv[1] == 'activate':
		print 'Received DOOR Activation code' 
		try:
			GPIO.output(7,True)
			time.sleep(4)
			GPIO.output(7,False)
		except Exception as e:
			print e, 'Failed to set GPIO'
	else:
		print 'Incorrect DOOR Activation password received' 
try:
	GPIO.cleanup()
except Exception as e:
	print e, 'GPIO cleanup error'
