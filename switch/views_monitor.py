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


def monitor_network(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'网络设备'
	i_user = request.COOKIES.get('starl', '')

	monitor_form = monitor_Form()
	onedate      = str(datetime.datetime.now() - datetime.timedelta(hours=2))[0:19]
	form         = Monitor.objects.filter(datatime__gte=onedate)
	
	return render_to_response('switch/monitor_network.html', {'switch_form':monitor_form,'form':form,'a_path':a_path,'i_user':i_user})

def monitor_server(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("monitor_server")
	