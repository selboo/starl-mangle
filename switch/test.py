#!/usr/bin/env python
#coding=utf-8
import os,sys,post_security
import re

link = post_security.telnetXKCS('192.168.253.2', 'guocan.xu', 'kukudeai&&(^123', '23', 'e16starl')
link.telnetInit()
link.telnetCiscoenable()


inte_input = link.telnetcmdmor('show interface Ethernet0/1 | in 1 minute input')
inte_ouput = link.telnetcmdmor('show interface Ethernet0/1 | in 1 minute output')
inte_pings = link.telnetcmdmor('ping 114.247.25.73 timeout 1 repeat 100')

_traffic_byts_re = re.compile( '(?<=\D)(\d*)(?= bytes/sec)' )
_traffic_pkts_re = re.compile( '(?<=\D)(\d*)(?= pkts/sec)'  )
_traffic_ping_re = re.compile( '(\d{1,5}/\d{1,5}/.\d{1,5})' )

def traffic( re_rule, linestr ):
    match = re_rule.findall( linestr )
    if match:
        return match[0]

input_byts = traffic( _traffic_byts_re, inte_input )
ouput_byts = traffic( _traffic_byts_re, inte_ouput )
input_pkts = traffic( _traffic_pkts_re, inte_input )
ouput_pkts = traffic( _traffic_pkts_re, inte_ouput )
pings = traffic( _traffic_ping_re, inte_pings ).split('/')

print input_byts, ouput_byts
print input_pkts, ouput_pkts
print pings


