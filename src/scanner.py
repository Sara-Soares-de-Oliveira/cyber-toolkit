#python version 3 
import socket 

host = "127.0.0.1"
portlist =[8000]

for port in portlist: 
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.settimeout(2)
	result = socket.connect_ex((host,port))

print(port, ":", result)
