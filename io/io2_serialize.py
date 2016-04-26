#!/usr/bin/env python

import json
try:
	import cPickle as pickle
except ImportError:
	import pickle


d=dict(name='Bob',age=20,score=80)
#print pickle.dumps(d)
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

print json.dumps(d)
