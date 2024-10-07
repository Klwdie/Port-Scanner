#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates hostname to ipv4 "python3 scanner.py cheese"

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>") #this does not ensure has a correct ip or octet length

#banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

#Not threaded
try:
	for port in range(50,85) #checks common ports; DNS (53) and HTTP (80)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #times out if a port doesn't respond back
		result = s.connect_ex((target,port)) #open = 0, closed port = 1 
		if result == 0:
			print(f"Port {port} is open.") #f string
		s.close() #closes the socket connection on that port

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit() #graceful exit
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit
