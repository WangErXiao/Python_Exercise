#!/usr/bin/evn python

class User(object):
	
	def a():pass
	
	@staticmethod
	def b():pass
	
	@classmethod
	def c(cls):pass

print User.a
print User.b
print User.c






class Student(object):
	def __new__(cls,*args,**kwargs):
		print "__new__",cls,args,kwargs
		return object.__new__(cls)
	
	def __init__(self,name,age):
		print "__init__",name,age
	
	def __del__(self):
		print "__del__"


u=Student("Tom",22)

del u















