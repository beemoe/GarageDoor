import RPi.GPIO as GPIO
import json
import socket
import time

#Create door state object
doorMap = {}

#Init gpio array.
gpioInputs = [18,17,25]
GPIO.setmode(GPIO.BCM)

#Socket class
class SocketOome(object):
    sock = None
    host = None
    socketConnected = False
    TCP_PORT = 7387

    def __init__(self):
        print("Inited")
        

    def connectSocket(self):
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.socketConnected = False
        while not self.socketConnected:
            try:
                self.sock.connect((self.host, self.TCP_PORT))
                self.sock.send('CONN')
                self.sock.flush
                self.socketConnected = True
                print("Connected to server!")
            except:
                print("Connection to " + socket.gethostname() + " failed miserably. Trying again in 2 sec. bro")
                time.sleep(2)

    def writeToSocket(self, message):
        try:
            self.sock.send(message)
        except socket.error:
            self.connectSocket()
            self.sock.send(message)
        
sockObj = SocketOome()
sockObj.connectSocket()

#Event callback for pin information
def pinChanged(channel):

    #update the map
    doorMap.update({channel:GPIO.input(channel)})
    sockObj.writeToSocket(json.dumps(doorMap))


#pin setups
for pin in gpioInputs:
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=pinChanged, bouncetime=200)
    doorMap[pin] = GPIO.input(pin)



raw_input()
GPIO.cleanup()
