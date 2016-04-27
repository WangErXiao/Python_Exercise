#!/usr/bin/env python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('google.com',80))
s.send('GET / HTTP/1.1\r\nHost:www.google.com\r\nConnection:close\r\n\r\n')

buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

s.close()

print buffer
