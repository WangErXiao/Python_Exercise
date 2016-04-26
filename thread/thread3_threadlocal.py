#!/usr/bin/env python

import threading
import time

local_people=threading.local()


def process(name):
	local_people.name=name
	time.sleep(3)
	print 'name is %s ,thread name is %s \r\n' % (local_people.name ,threading.current_thread().name)


t1=threading.Thread(target=process,args=('yao',),name='thread1')
t2=threading.Thread(target=process,args=('robin',),name='thread2')
	

t1.start()
t2.start()

t1.join()
t2.join()

	
