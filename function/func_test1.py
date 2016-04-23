#!/usr/bin/env python

def test(name):
	if name =="a":
		print 'name is a'
		def a():pass
		return a
	else:
		print 'name is b'
		def b():pass
		return b

print 'test("a").__name__ is %s' % test("a").__name__
