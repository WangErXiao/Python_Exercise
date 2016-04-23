#!/usr/bin/env python

d={'Tom':100,'Jim':22,'Lucy':99}

print ' Tom score is :%d' % d['Tom']
print ' Jim score is :%d' % d.get('Jim')

d.pop('Lucy')
print 'dict is : %s' % d
