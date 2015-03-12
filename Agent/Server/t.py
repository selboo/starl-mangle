#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import os

a = '''
1234567890abcdefghijklmnopqrstuvwxyzABCDEFG123
1234567890abcdefghijklmnopqrs
tuvwxyzABCDEFG123
1234567890abcdefghijklmnopqrstuvwxyzABCDEFG1231234567890abcdefghijkl
mnopqrstuvwxyzABCDEFG1231234567890abcdefghijklmnop
qrstuvwxyzABCDEFG1231234567890abc
defghijklmnopqrstuvwxyzABCDEFG123
1231234567890123'''

tcp_limit  = 3
tcp_length = len(a)
tcp_Subcon = tcp_length / tcp_limit
tcp_tail   = tcp_length % tcp_limit


number_start = 0
number_stop  = tcp_limit

print '几段',tcp_limit
print '长度',tcp_length
print '段数',tcp_Subcon
print '余数',tcp_tail
alist = []
print '-------------------------------'

for i in range(0,tcp_Subcon):
	alist.append(a[number_start:number_stop])
	number_start = number_stop
	number_stop  = number_stop + tcp_limit

print a[number_start:number_stop+tcp_tail]
alist.append(a[number_start:number_start+tcp_tail])
print '==================================='
print a
print alist
print "".join(alist)


#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGH
#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGH

