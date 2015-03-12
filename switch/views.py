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

def switch(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'网络设备'
	i_user = request.COOKIES.get('starl', '')

	switch_form = switch_Form()
	form = Switch.objects.filter()
	return render_to_response('switch/switch.html', {'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})

	
def switch_add(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'添加网络设备'
	i_user = request.COOKIES.get('starl', '')


	if request.method == 'POST':
		form = switch_add_Form(request.POST)
		if form.is_valid():
			name      = form.cleaned_data['name']
			switch_ip = form.cleaned_data['switch_ip']
			user      = form.cleaned_data['user']
			password  = form.cleaned_data['password']
			enable    = form.cleaned_data['enable']
			sw_type   = form.cleaned_data['sw_type']
			model     = form.cleaned_data['model']
			speed     = form.cleaned_data['speed']
			post      = form.cleaned_data['post']

			Switch.objects.create(	name      = name,
									switch_ip = switch_ip,
									user      = user,
									password  = password,
									enable    = enable,
									sw_type   = sw_type,
									model     = model,
									speed     = speed,
									post      = post)
			return HttpResponseRedirect("/switch/")

		else:
			return render_to_response('user_add.html',{'form':form,'error':'添加失败！！！','alert':'alert-error'})
	else:
		form = switch_add_Form()
		return render_to_response('switch/switch_add.html', {'form':form,'a_path':a_path,'i_user':i_user})
	
def switch_view(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("switch_view")
	
def switch_edit(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("switch_edit")
	
def switch_delete(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("switch_delete")

def switch_bonding(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'网卡绑定'
	i_user = request.COOKIES.get('starl', '')

	switch_form = switch_Form()
	form = Switch.objects.filter(name__startswith='BJ_Switch')
	step = 1

	if request.method == 'POST':
		form = Switch_bonding(request.POST)
		if form.is_valid() and int(form.cleaned_data['step']) == 2:
			step      = 2
			global host,userid,passwd,enpasswd,post,port
			global ip,link,switch_name

			name = form.cleaned_data['name']
			ip   = form.cleaned_data['ip']
			post = form.cleaned_data['post']

			ini         = Switch.objects.get(switch_ip=ip)
			host        = str(ini.switch_ip)
			userid      = str(ini.user)
			passwd      = str(ini.password)
			enpasswd    = str(ini.enable)
			switch_name = str(ini.name)
			post        = int(ini.post)
			port        = 23

			link = post_security.telnetXKCS(host , userid , passwd ,  port , enpasswd)
			link.telnetInit()
			link.telnetCiscoenable()

			interface_init = link.telnetcmdmor('show interface status')
			_re_interface_ = re.compile( 'Fa0/(\d{1,2})\s*(connected|notconnect)\s*(\d{1,3})' )
			interface_all = _re_interface_.findall(interface_init)

			#switch_2 = []

			#for i in range(1,post):
			#	get_mac     = link.telnetcmdmor('show running-config interface Fa0/%s' %i)
			#	_get_mac_re = re.compile( "\w{1,4}\.\w{1,4}\.\w{1,4}" )
			#	inte_list   = list(interface_all[i-1])
			#	inte_list.append(_get_mac_re.findall(get_mac))
			#	switch_2.append(inte_list)
			
			switch_2 = interface_all
			return render_to_response('switch/switch_bonding.html', {'switch_2':switch_2,'step':step,'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})
		
		if form.is_valid() and int(form.cleaned_data['step']) == 3:
			step       = 3
			int_status = form.cleaned_data['int_status']
			int_post   = form.cleaned_data['int_post']
			int_vlan   = form.cleaned_data['int_vlan']

			interface_mac = link.telnetcmdmor('show running-config interface Fa0/%s' %int(int_post) )
			_interface_mac_re = re.compile( "\w{1,4}\.\w{1,4}\.\w{1,4}" )
			if len(_interface_mac_re.findall(interface_mac)) >= 1:
				int_mac = _interface_mac_re.findall(interface_mac)[0]
			else:
				int_mac = ""

			interface_re = link.telnetcmdmor('show port-security interface Fa0/%s' %int(int_post) )
			_interface_re_re = re.compile( "\w{1,4}\.\w{1,4}\.\w{1,4}" )
			int_mac_lost = _interface_re_re.findall(interface_re)[0]

			switch_3 = [switch_name, ip, int_post, int_vlan, int_mac, int_mac_lost]

			return render_to_response('switch/switch_bonding.html', {'switch_3':switch_3,'step':step,'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})

		if form.is_valid() and int(form.cleaned_data['step']) == 4:
			step           = 4
			switch_db_name = form.cleaned_data['switch_db_name']
			switch_bd_post = form.cleaned_data['switch_bd_post']
			switch_bd_vlan = form.cleaned_data['switch_bd_vlan']
			switch_bd_mac  = form.cleaned_data['switch_bd_mac']
			switch_bd_ip   = form.cleaned_data['switch_bd_ip']

			switch_4 = []
			if switch_bd_vlan != "":
				link.telnetcmdmor('configure terminal')
				link.telnetcmdmor('interface Fa0/%s' %int(switch_bd_post))
				link.telnetcmdmor('switchport mode access')
				link.telnetcmdmor('switchport access vlan %s' %int(switch_bd_vlan))
				switch_4.append('Vlan Exchange ok...')
				
			if switch_bd_mac  != "":
				link.telnetcmdmor('configure terminal')
				link.telnetcmdmor('interface Fa0/%s' %int(switch_bd_post))
				link.telnetcmdmor('no switchport mode access')
				link.telnetcmdmor('no switchport port-security')
				link.telnetcmdmor('no switchport port-security mac-address')
				link.telnetcmdmor('no switchport port-security maximum')
				link.telnetcmdmor('no switchport port-security violation shutdown')
				link.telnetcmdmor('switchport mode access')
				link.telnetcmdmor('switchport port-security')
				link.telnetcmdmor('switchport port-security mac-address %s' %str(switch_bd_mac))
				link.telnetcmdmor('switchport port-security maximum 1')
				link.telnetcmdmor('switchport port-security violation shutdown')
				switch_4.append('Vlan Port-Security ok...')


			if switch_bd_ip   != "":
				linkcore = post_security.telnetXKCS('192.168.192.1' , userid , passwd ,  port , enpasswd)
				linkcore.telnetInit()
				linkcore.telnetCiscoenable()
				linkcore.telnetcmdmor('configure terminal')
				linkcore.telnetcmdmor('arp %s %s ARPA' %(str(switch_bd_ip),str(switch_bd_mac)))
				switch_4.append('Vlan ARP ok...')

			return render_to_response('switch/switch_bonding.html', {'switch_4':switch_4,'step':step,'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})

	else:
		return render_to_response('switch/switch_bonding.html', {'step':step,'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})

def switch_arp(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("switch_bonding")

def switch_tools(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'网络设备'
	i_user = request.COOKIES.get('starl', '')

	switch_form = switch_Form()
	form = Switch.objects.filter()
	ip_list = []

	
	for item in form:
		#print item.switch_ip
		ip_list.append(item.switch_ip)
	print ip_list


	return render_to_response('switch/switch_tools.html', {'ip_list':ip_list,'switch_form':switch_form,'form':form,'a_path':a_path,'i_user':i_user})
