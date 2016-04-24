#!/usr/bin/env python

class User(object):
	table="t_user"
	def __init__(self,name,age):
		self.name = name
		self.age  = age


print User.table
u1=User("user1",18)
print u1.table
print u1.__dict__
u2=User("user2",11)
print u2.__dict__

print User.__dict__

