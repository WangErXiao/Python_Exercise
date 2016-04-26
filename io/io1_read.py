#!/bin/usr/env python

try:
	f=open('print_josn.py','r')
	print f.read()

finally:
	if f:
		f.close()
