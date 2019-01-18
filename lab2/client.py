#!/usr/bin/env python3
import socket
import sys

#80 is the main http port
HOST, PORT  = "www.google.com", 80
payload = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(HOST)
BUFFER_SIZE = 1024

#creates a new socket
def get_request(addr):
	(family, sock_type, proto, canonname, sockaddr) = addr
	try:
		s = socket.socket(family, sock_type, proto)
		s.connect(sockaddr)
		s.sendall(payload.encode()) # encode sends it in bytes
		s.shutdown(socket.SHUT_WR)
		full_data = b""
		while True:
			data = s.recv(BUFFER_SIZE)
			if not data: break
			full_data += data
		print(full_data)
	except Exception as e:
		print(e)
	finally:
		s.close()


def main():
	addr_info = socket.getaddrinfo(HOST, PORT)
	for addr in addr_info:
		(family, sock_type, proto, canonname, sockaddr) = addr
		if family == socket.AF_INET and sock_type == socket.SOCK_STREAM:
			print(addr)
			get_request(addr)

'''data = " ".join(sys.argv[1:])

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
'''

if __name__ == "__main__":
	main()
