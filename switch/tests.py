#!/usr/bin/env python
#coding=utf-8
import os,sys,post_security
import re

#link = post_security.telnetXKCS('192.168.192.5', 'guocan.xu', 'kukudeai&&(^123', '23', 'e16starl')
#link.telnetInit()
#link.telnetCiscoenable()

#inte_input = link.telnetcmdmor('show interface status')

a="""
Fa0/1                        notconnect   230          auto   auto 10/100BaseTX
Fa0/2                        notconnect   230          auto   auto 10/100BaseTX
Fa0/3                        notconnect   230          auto   auto 10/100BaseTX
Fa0/4                        notconnect   230          auto   auto 10/100BaseTX
Fa0/5                        notconnect   230          auto   auto 10/100BaseTX
Fa0/6                        connected    80         a-full  a-100 10/100BaseTX
Fa0/7                        connected    230        a-full   a-10 10/100BaseTX
Fa0/8                        connected    230        a-full  a-100 10/100BaseTX
Fa0/9                        connected    290        a-full   a-10 10/100BaseTX
Fa0/10                       notconnect   230          auto   auto 10/100BaseTX
Fa0/11                       notconnect   320          auto   auto 10/100BaseTX
Fa0/12                       connected    20         a-full  a-100 10/100BaseTX
Fa0/13                       connected    90         a-full  a-100 10/100BaseTX
Fa0/14                       notconnect   310          auto   auto 10/100BaseTX
Fa0/15                       connected    20         a-full  a-100 10/100BaseTX
Fa0/16                       connected    290        a-full  a-100 10/100BaseTX
Fa0/17                       connected    90         a-full   a-10 10/100BaseTX
Fa0/18                       connected    90         a-full  a-100 10/100BaseTX
Fa0/19                       connected    90         a-full  a-100 10/100BaseTX
Fa0/20                       connected    290        a-full   a-10 10/100BaseTX
Fa0/21                       connected    90         a-full  a-100 10/100BaseTX
Fa0/22                       notconnect   290          auto   auto 10/100BaseTX
Fa0/23                       connected    100        a-full  a-100 10/100BaseTX
Fa0/24                       connected    90         a-full  a-100 10/100BaseTX
Gi0/1                        connected    trunk      a-full  a-100 10/100/1000BaseTX
Gi0/2                        notconnect   1            auto   auto 10/100/1000BaseTX
"""

_t_re = re.compile( 'Fa0/(\d{1,2})\s*(connected|notconnect)\s*(\d{1,3})'  )

def traffic( re_rule, linestr ):
    match = re_rule.findall( linestr )
    if match:
        return match[0]

ouput_pkts = traffic( _t_re, a )
#print ouput_pkts





#print _t_re.findall( a )


a1 = [('1', 'notconnect', '230'), ('2', 'notconnect', '230'), ('3', 'notconnect', '230'), ('4', 'notconnect', '230'), ('5', 'notconnect', '230'), ('6', 'connected', '80'), ('7', 'connected', '230'), ('8', 'connected', '230'), ('9', 'connected', '290'), ('10', 'notconnect', '230'), ('11', 'notconnect', '320'), ('12', 'connected', '20'), ('13', 'connected', '90'), ('14', 'notconnect', '310'), ('15', 'connected', '20'), ('16', 'connected', '290'), ('17', 'connected', '90'), ('18', 'connected', '90'), ('19', 'connected', '90'), ('20', 'connected', '290'), ('21', 'connected', '90'), ('22', 'notconnect', '290'), ('23', 'connected', '100'), ('24', 'connected', '90')]
switch_2 = []
print len(a1)
for i in range(1,25):
	a = list(a1[i-1])
	switch_2.append(a)

print switch_2


#print type(a)
def interfaceport ( arpstr ):
	for line in arpstr:
		#print line
		interface = traffic( _t_re, line )
	return interface

#print a
#s = traffic( _t_re, a ).split(' ')
#s = interfaceport(a)
#list1=[x for x in s if x.strip()]
#print s
#print list1

#print re.findall('Fa0/(.*?)TX', a) 


#interface_mac = link.telnetcmdmor('show running-config interface Fa0/5')
#_interface_mac_re = re.compile( "\w{1,4}\.\w{1,4}\.\w{1,4}" )
#if len(_interface_mac_re.findall(interface_mac)) >= 1:
#	int_mac = _interface_mac_re.findall(interface_mac)[0]
#else:
#	int_mac = ""

#print int_mac

