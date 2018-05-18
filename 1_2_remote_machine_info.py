#! /user/bin/env python3
import socket

def get_remote_machine_info(domainName):
	try:
		print('IP address of %s: %s'%(domainName,
		socket.gethostbyname(domainName)))
	except socket.error as err_msg:
		print('%s:%s'%(domainName,err_msg))
domainName=(input("Enter domain name you want to search: "))

get_remote_machine_info(domainName)

