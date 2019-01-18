#!/usr/bin/env python3

#receive a connection, receive some data, then echo it back

import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
	google_addr = None

	addr_info = socket.getaddrinfo("www.google.com", PORT)
	for addr in addr_info:
		(family, sock_type, proto, canonname, sockaddr) = addr
		if family == socket.AF_INET and sock_type == socket.SOCK_STREAM:
			google_addr = addr

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen(1) # listen one at a time
		while True:
			conn, addr = s.accept()	
			print("Connected by", addr)
			
			(family, sock_type, proto, canonname, sockaddr) = google_addr
			with socket.socket(family, sock_type) as proxy_end:
				proxy_end.connect(sockaddr)
				send_full_data = b""
				while True:
					data = conn.recv(BUFFER_SIZE)
					if not data: break
					send_full_data += data
					conn.send(data)
				proxy_end.sendall(send_full_data)
				proxy_end.shutdown(socket.SHUT_WR)

				while True:
					data = proxy_end.recv(BUFFER_SIZE)
					if not data : break
					conn.send(data)

			time.sleep(0.5)
			conn.close()

if __name__ == "__main__":
	main()