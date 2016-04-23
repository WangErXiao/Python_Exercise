#!/usr/bin/env python

def consumer():
	while True:
		d=yield
		if not d:break
		print "consumer:",d


c=consumer()
c.send(None)
c.send(1)
c.send(2)
c.send(3)
