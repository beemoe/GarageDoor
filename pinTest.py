import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def pinChanged(channel):
	if(GPIO.input(channel)):
		print str(channel) + " closed"
	else:
		print str(channel) + " open"

GPIO.add_event_detect(18, GPIO.BOTH, callback=pinChanged, bouncetime=200)
GPIO.add_event_detect(23, GPIO.BOTH, callback=pinChanged, bouncetime=200)
GPIO.add_event_detect(24, GPIO.BOTH, callback=pinChanged, bouncetime=200)

if(GPIO.input(18)):
	print "Door 1 is closed"
else:
	print "Door 1 is open"
	
if(GPIO.input(23)):
	print "Door 2 is closed"
else:
	print "Door 2 is open"
	
if(GPIO.input(24)):
	print "Door 3 is closed"
else:
	print "Door 3 is open"


	
raw_input()
GPIO.cleanup()
