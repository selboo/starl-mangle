import os,sys

class aa():
	def __init__( self,debug = '3' ):

		self.debug = debug

	def telnetInit( self , host = self.debug ):
		print self.debug
		print host


bbb = '192'
v=aa('233')
v.telnetInit('333')