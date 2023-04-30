#!/bin/python3

import sys #Allow to enter arguments in command line
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Traslate hostname to ipv4
else:
	print('Invalid amount of arguments.')
	print('Systanx: python scanner.py <ip>')
	sys.exit()
	
#Banner
print('=' * 50)
print('Scanning Target: ' + target)
print('Time Started: ' +str(datetime.now()))
print('=' * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print('Checking port {}'.format(port))
		if result == 0:
			print('Port {} is open'.format(port))
		s.close()
except KeyboardInterrupt:
	print('\nExiting the program')
	sys.exit()

except socket.gaierror:
	print('\nHostname cant be resolved.')
	sys.exit()
	
except socket.error:
	print('\nCouldnt connect to server.')
	sys.exit()
