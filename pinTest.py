import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(25, GPIO.IN)


def pinChanged(channel):
	if(GPIO.input(channel)):
		print str(channel) + " circuit open!"
	else:
		print str(channel) + " circuit closed"

GPIO.add_event_detect(18, GPIO.BOTH, callback=pinChanged, bouncetime=200)
GPIO.add_event_detect(17, GPIO.BOTH, callback=pinChanged, bouncetime=200)
GPIO.add_event_detect(25, GPIO.BOTH, callback=pinChanged, bouncetime=200)


	
raw_input()
GPIO.cleanup()
