import os,sys


class a:
	def __init__(self):
		self.a='123'
		self.b='222'

	def pr(self):
		print self.a
		print self.b

	def __sy(self):
		print self.a
bb = a()
bb.pr()

aa='22'

try:
    f = open('l2.py')
except:
    a='123'
    #error='22'
    #print 'open falid'


a=[1,2,'t','d','g54rt','t2',[1,3,5,2]]
for i in a:
	print type(i)
	if type(i) == type('s'):
		print 'p1111111'
	else:
		print '222222'

