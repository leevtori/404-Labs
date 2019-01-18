#!/usr/bin/env python3

#receive a connection, receive some data, then echo it back

import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen(1) # listen one at a time
		while True:
			conn, addr = s.accept()	
			print("Connected by", addr)
			
			full_data = b"" # empty byte string
			while True:
				data = conn.recv(BUFFER_SIZE)
				#print(data)
				if not data: break
				full_data += data

			time.sleep(0.51)
			conn.sendall(full_data)
			conn.close()

if __name__ == "__main__":
	main()