#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import sys,os
from daemon import Daemon
from server import start

class MyDaemon(Daemon):
	def run(self):
		print 'start'
		start()
		print 'stop2'
 
if __name__ == "__main__":
	daemon = MyDaemon()
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)


