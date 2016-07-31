import RPi.GPIO as GPIO
import json
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 7387
BUFFER_SIZE = 1024


#Door Map
doorMap = {}
gpioInputs = [18,17,25]

GPIO.setmode(GPIO.BCM)

#GPIO.setup(18, GPIO.IN)
#GPIO.setup(17, GPIO.IN)
#GPIO.setup(25, GPIO.IN)

def pinChanged(channel):

    doorMap.update({channel:GPIO.input(channel)})

    if GPIO.input(channel):
		msg = str(channel) + " circuit open!"
    else:
		msg = str(channel) + " circuit closed!"
    
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    sock.send(json.dumps(doorMap))
    sock.close()

    #pin setups
for pin in gpioInputs:
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=pinChanged, bouncetime=200)
    doorMap[pin] = GPIO.input(pin)

#GPIO.add_event_detect(18, GPIO.BOTH, callback=pinChanged, bouncetime=200)
#GPIO.add_event_detect(17, GPIO.BOTH, callback=pinChanged, bouncetime=200)
#GPIO.add_event_detect(25, GPIO.BOTH, callback=pinChanged, bouncetime=200)

	
raw_input()
GPIO.cleanup()
