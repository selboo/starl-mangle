#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context, RequestContext
from django.core.mail import send_mail

from starl.forms import *
from starl.models import *
from starl.views import *

from switch.forms import *
from switch.models import *
from switch.views import *

import re,datetime,time
import post_security

def monitor_tarffic(request):
	del request.session
	Asa_ini  = Switch.objects.get(name='BJ_Asa')
	host     = str(Asa_ini.switch_ip)
	userid   = str(Asa_ini.user)
	passwd   = str(Asa_ini.password)
	enpasswd = str(Asa_ini.enable)
	port     = 23

	link = post_security.telnetXKCS(host , userid , passwd ,  port , enpasswd)
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
	pings      = traffic( _traffic_ping_re, inte_pings ).split('/')


	Monitor.objects.create(
							ip             = '192.168.253.2',
							datatime       = str(datetime.datetime.now())[0:19],
							traffic_input  = input_byts,
							traffic_output = ouput_byts,
							packets_input  = input_pkts,
							packets_output = ouput_pkts,
							ping_min       = pings[0],
							ping_avg       = pings[1],
							ping_max       = pings[2],
	)

	return HttpResponse('ok')


