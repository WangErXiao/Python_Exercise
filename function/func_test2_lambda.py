#!/usr/bin/env python

add = lambda x=0,y=0:x+y

print 'lambda add(1,2) result is %d' % add(1,2)
print 'lambda add() result is %d' % add()
print 'lambda add(1) result is %d' % add(1)


m=map(lambda x:x%2 and None or x, range(10))
print 'map m is %s' % m
