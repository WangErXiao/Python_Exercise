#!/usr/bin/evn python

import time




def log(func):
	def wrapper(*args,**kw):
		print 'call %s()' % func.__name__
		return func(*args,**kw)
	
	return wrapper

@log
def now():
	print time.time()

now()