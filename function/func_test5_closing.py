#!/usr/bin/env python

'''

'''

def test():
	x=[1,2]
	def a():
		x.append(3)
		print 'x is %s ' % x

	def b():
		print 'x is %s ' % x

	return a,b


a,b= test()
a()
b()


def test1():
	for i in range(3):
		def a():
			print i
		yield a


m,n,z=test1();

m()
n()
z()


