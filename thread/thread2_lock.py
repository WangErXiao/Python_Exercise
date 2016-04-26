#!/usr/bin/evn python

import threading

counter=0
lock=threading.Lock()

def update_counter(n):
	global counter
	lock.acquire()
	try:
		i=1
		while(i<=n):
			counter+=1
			i+=1
			print counter , 'lock is %s' % threading.current_thread().name

	finally:
		lock.release()


t1=threading.Thread(target=update_counter,args=(100,),name='Thread1')

t2=threading.Thread(target=update_counter,args=(300,),name='Thread2')
t1.start()
t2.start()
t1.join()
t2.join()













