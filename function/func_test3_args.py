#!/usr/bin/env python

# default parameter

def test(x,ints=[]):
	ints.append(x)
	return ints

def mytest(a,b,*args,**kwargs):
	print a,b
	print args
	print kwargs

mylambda=lambda a,b=0,*args,**kwargs :	sum([a,b]+list(args)+kwargs.values())


print 'result is %s ' % test(1)
print 'result is %s ' % test(2)
print 'result is %s ' % test(3)
print 'result is %s ' % test(3)
print 'result is %s ' % test(3)

mytest(1,2,'a','b','c',x=100,y=200)

mytest(*range(1,8),**{'x':'hello','y':'world'})

mylambda(1,*[2,3,4],**{'x':5,'y':6})





