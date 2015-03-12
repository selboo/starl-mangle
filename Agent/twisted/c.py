#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8

from twisted.internet import protocol, reactor
from twisted.internet.protocol import Factory,Protocol
from time import ctime


class TCPServer(protocol.Protocol):
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print '...connected from:', clnt
	def dataReceived(self, data):
		self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TCPServer

print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()



	