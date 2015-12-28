
#Server


import datetime
import os, sys
from twisted.internet import protocol, reactor
import thread
import threading




#def GpsTimeRun():
#	while(True):
#		os.system("gpspipe -n 5 -w -o gpstime.txt")
#		f = open("gpstime.txt", "r")
#		for line in f:
#			if line.find("time") > -1:
#				if line.find("lat") > -1:
#					if int(line[line.index("lat") + 5: line.index("lat") + 14]) > 20.5:
#						if int(line[line.index("lat") + 5: line.index("lat") + 14]) < 48:
#							time = "date -s " + line[line.index("time") + 7: line.index("time") + 31]	
#							os.system(time)
#		os.system("rm gpstime.txt")
	









#os.system("ifconfig eth0 192.168.1.100 netmask 255.255.255.0")
os.system("python gpstime.py")



class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(str(datetime.datetime.now()))
		





class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()




#thread.start_new_thread(GpsTimeRun, ())



reactor.listenTCP(9000, EchoFactory())
reactor.run()
