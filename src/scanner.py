# Adapted from the TCP port scanning example in Python Penetration
# Testing Essentials, Packt Publishing, January 2015.
# ISBN: 978-1-78439-858-3.
#
# I adapted the example to Python 3 and tested it with a local HTTP
# server on Kali Linux, comparing the results with the server running
# and stopped.
#python version 3 
import socket 

host = "127.0.0.1"
portlist =[8000]

for port in portlist: 
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.settimeout(2)
	result = socket.connect_ex((host,port))

print(port, ":", result)
