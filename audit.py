#!/usr/bin/python

import os, sys, socket, argparse
from datetime import datetime

#Vars
canreadpass = False
redtext = "\033[31m"
whitetext = "\033[39m"
starttime = datetime.now()
format = "%d/%m/%Y %H:%M:%S"
parser = argparse.ArgumentParser()

def banner():
	print ("Security Audit Script")
	print ("Created by Kieran Baumann")
	print ("Script ran at " + starttime.strftime(format))

#arguments
parser.add_argument("help")
parser.parse_args()




#os.system to run commands
#info = os.system('uname -snrmo')
def osinfo():
	print("\nOperating Information")
	infoName = ["Kernal Name : ", "Computer Name : ", "Release : ", "Version : ", "Architecture :"]
	for i in range(0,5):
		osinfo = "[+]" + infoName[i] + os.uname()[i]
		print(osinfo)


def filecheck():
	print ("\nChecking files")
	files = ["/etc/shadow", "/etc/passwd", "/etc/bashrc", "/etc/fstab", "/etc/hosts", "/etc/securetty", "/proc/filesystems", "/proc/ioports/", "/proc/modules", "/var/log/messages"] #append for more files
	for file in files:
		if os.access(file, os.R_OK):
			print (redtext + "[-]" + file + " can be read" + whitetext)
			#add to list and print in report!!!!
		else:
			print ("[+]" + file + " can not be read")


def checkpip():
	print ("\nPip Packages")
	try:
		print (os.system('pip list'))
	except Exception as e:
		print ("[+]"+ "Pip not installed")
		print (e)


def getlocalIP():
	print ("\nChecking Ports")
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket object
	s.connect(("8.8.8.8", 80)) #connect to the socket
	localip = s.getsockname()[0]
	print ("Scanning Ports on " + localip) #print local ip for scanning
	checkports(localip)
	s.close()


def checkports(localip):
	try:
		for port in range(1,5): #all ports between 1,arg
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
			socket.setdefaulttimeout(0.1) #set timeout to increase time
			result = s.connect_ex((localip, port)) #result from connecting to ip, port
			#check if port is open
			if result == 0:
				print("Port {} is open".format(port))
			else:
				print("Port {} is closed".format(port))
			s.close()
			
	except KeyboardInterrupt:
		print("\n Quitting")
		sys.exit()



def report():
	print("---------------------")
	print ("report")

def script_usermode():
	banner() #prints banner
	osinfo() #prints operating system information
	filecheck() #checks if important files are readable
	getlocalIP()
	checkpip()
	report()

script_usermode()

#arguments
#print pip installs
#ports open
#check home directories etc
#help


