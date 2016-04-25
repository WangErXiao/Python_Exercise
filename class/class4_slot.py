#!/usr/bin/env python

class Student(object):
	__slots__=('name','age')

s=Student()
s.name='yao'
s.age=22

print s.name,s.age

s.score=11
