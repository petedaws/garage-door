from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.application.internet import TCPServer
from twisted.application.service import Application

import RPi.GPIO as GPIO
import time
import sys

GARAGE = 7
PASSWD_PATH = '/home/pi/garage-door/password'

class Trigger(Resource):
	def __init__(self,password):
		self.password = open(password,'r').read().strip()

	def render_POST(self, request):
		if self.password == request.content.read().decode('utf-8'):
			print('success')
			GPIO.output(GARAGE,False)
			time.sleep(1)
			GPIO.output(GARAGE,True)
		else:
			print('fail')
		return b'<html></html>'

try:
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GARAGE,GPIO.OUT,initial=True)
except Exception as e:
	print(e, 'Failed to setup GPIO')
	exit(0)

garage = Resource()
garage.putChild(b"trigger",Trigger(PASSWD_PATH))
root = Resource()
root.putChild(b"garage", garage)
factory = Site(root)
application = Application("gdo")
server = TCPServer(8001, factory)
server.setServiceParent(application)
