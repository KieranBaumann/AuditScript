#!/usr/bin/python

import os, sys, socket
from datetime import datetime

#Vars
canreadpass = False
redtext = "\033[31m"
whitetext = "\033[39m"
timenow = datetime.now()
format = "%d/%m/%Y %H:%M:%S"
#print banner
def banner():
	print ("Security Audit Script")
	print ("Created by Kieran Baumann")
	print ("Script ran at " + timenow.strftime(format))

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
	print ("Scanning Ports" + localip) #print local ip for scanning
	checkports(localip)
	s.close()

def checkports(localip):
	for port in range(1,1025)


def report():
	print("---------------------")
	print ("report")

def script_usermode():
	banner() #prints banner
	osinfo() #prints operating system information
	filecheck() #checks if important files are readable
	checkpip()
	getlocalIP()
	report()

script_usermode()


#print pip installs
#ports open
#check home directories etc
#help


