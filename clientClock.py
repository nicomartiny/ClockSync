
#version 1.2

import sys,os
import datetime
import time
from twisted.internet.protocol import Protocol
from sys import stdout
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor




#start of socket

time_tuple = ""

#serverIpAddress = str(raw_input("Enter server IP: "))
#serverPort = int(raw_input("Enter server port: "))
serverIpAddress = "192.168.1.10"
serverPort = 9000


class clockClient(Protocol):
    def connectionMade(self):
        self.transport.write("GREETING")
        self.greetingComplete = Deferred()
        print("Connection made")
               


    def dataReceived(self, bytes):
        # this puts the output from one computer into this one
    
        time_tuple = bytes
        
        print("Time recieved", time_tuple)
        
        time_tuple = time_tuple.split(" ")
	if sys.platform=='linux2':
        	sysTime = 'date -s ' + time_tuple[1]
	if sys.platform=='win32':
		sysTime = 'time ' + time_tuple[1]
        os.system(sysTime)
	time.sleep(5)
	self.connectionMade()
    





f = Factory()
f.protocol = clockClient

e = TCP4ClientEndpoint(reactor, serverIpAddress, int(serverPort))
d = e.connect(f)

reactor.run()

