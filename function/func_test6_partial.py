#!/usr/bin/env python

from functools import partial

def test(a,b,c):
	print a,b,c


f= partial(test,b=3,c=2)
f(1)
