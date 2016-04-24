#!/usr/bin/env python

def _private_method1():
	print 'private method 1'

def _private_method2():
	print 'private method 2'


def hello(arg):
	if arg==1:
		_private_method1()
	else:
		_private_method2()




hello(1)	
