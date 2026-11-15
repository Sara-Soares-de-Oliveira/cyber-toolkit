# Adapted from the TCP port scanning example in Python Penetration
# Testing Essentials, Packt Publishing, January 2015.
# ISBN: 978-1-78439-858-3.
#
# I adapted the example to Python 3 and tested it with a local HTTP
# server on Kali Linux, comparing the results with the server running
# and stopped.
#python version 3 
import socket 

host = input("Enter the ip address:")
portlist =[8000]

for port in portlist: 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.settimeout(5)
		result=sock.connect_ex((host,port))
		if result == 0:
			print("Connection accepted for port", port, "- code:", result)
		elif:
			print("Connection failed for port", port, "- code:", result)			
		
	except socket.error:
		print("Connection Error")	
	finally:	
		sock.close()


