from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

import RPi.GPIO as GPIO
import time
import sys

GARAGE = 7

class Trigger(Resource):
	def render_POST(self, request):
		if open('password','r').read().strip() == request.content.read():
			GPIO.output(GARAGE,True)
			time.sleep(1)
			GPIO.output(GARAGE,False)
		return '<html></html>'

if __name__ == "__main__":	
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(GARAGE,GPIO.OUT)
		GPIO.output(GARAGE,False)
	except Exception as e:
		print e, 'Failed to setup GPIO'
		exit(0)
	
	garage = Resource()
	garage.putChild("trigger",Trigger())
	root = Resource()
	root.putChild("garage", garage)
	factory = Site(root)
	reactor.listenTCP(8001, factory)
	reactor.run()
