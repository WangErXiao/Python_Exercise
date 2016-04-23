#!/usr/bin/env python
names=['tom','cat','lucy']
length= len(names)
print "list length is :" , length;
print 'list length is :%d' % len(names)
print 'index 1 of names is %s' %names[1]

names.append('robin')
print 'list length is :%d' % len(names)

names.insert(1,'yao')
print names
