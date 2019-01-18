#!/usr/bin/env python3
import socket

#80 is the main http port
HOST, PORT  = "localhost", 8001
payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
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

if __name__ == "__main__":
	main()
