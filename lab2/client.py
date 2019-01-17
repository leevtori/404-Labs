import socket
import sys

HOST, PORT  = "www.google.com", 80
data = " ".join(sys.argv[1:])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket sucessfully created")

try: 
	client.connect((HOST, PORT))
	print('socket sucessfully connected to google on port ==')

	client.sendall(bytes(data + "\n", "utf-8"))
	received = client.recv(1024)

finally :
	client.close()

print("sent	{}".format(data))
print("received {}".format(received))
