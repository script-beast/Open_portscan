#!/bin/python3
import sys
import socket
from datetime import datetime
#traget info :
if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
        print("Invalid statement")
        print("Syntax :- Python3 portscan.py <ip>")
        sys.exit("Exiting........")
start=0
en=0
option=100
while(option>4):
        print('-'*100)
        print("""
        Scanning {}
        
        Select Port :
        1. Common Ports (0 - 1023) (Recommended)
        2. All Ports (0-65353) (Slower)
        3. Specific Ports
        4.Exit
        
        """.format(sys.argv[1]))
        print("Enter the option to start the scan :-  ")
        option = int(input())
        if option == 1:
                en=1023
        elif option == 2:
                en=65353
        elif option == 3:
                print("Enter the starting value :- ")
                start=int(input())
                print("Enter the ending value :- ")
                en=int(input())
        elif option == 4:
                sys.exit("Exiting..............")
        else:
                print("Invalid Option")
print('-'*100)
print("Scanning " + target)
print("Time Started :- " + str(datetime.now()) )
print('-'*100)
try:
        for port in range(start,en+1):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result=s.connect_ex((target,port))
                if result == 0:
                        print("Port: {} is open".format(port))
                s.close()
except KeyboardInterrupt:
	print("\n Exiting Program .............")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resloved")
	sys.exit()
except socket.error:
        print ("couldn't connect to sever")
        sys.exit()