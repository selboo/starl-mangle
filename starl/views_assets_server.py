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
from forms import *

import re,datetime,time

def assets_server(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'设备资产'
	i_user = request.COOKIES.get('starl', '')

	assets_server_form = assets_server_add_Form()
	form = Assets_Server.objects.filter()
	return render_to_response('assets_server.html', {'form':form,'assets_server_form':assets_server_form,'a_path':a_path,'i_user':i_user})

def assets_server_add(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'设备资产'
	i_user = request.COOKIES.get('starl', '')
	
	if request.method == 'POST':
		form = assets_server_add_Form(request.POST)
		if form.is_valid():

			assets_server_data                 = Assets_Server()
			assets_server_data.Room            = form.cleaned_data['Room']
			assets_server_data.System          = form.cleaned_data['System']
			assets_server_data.Type            = form.cleaned_data["Type"]
			assets_server_data.Use             = form.cleaned_data["Use"]
			assets_server_data.Brand           = form.cleaned_data["Brand"]
			assets_server_data.Equipment_Model = form.cleaned_data["Equipment_Model"]
			assets_server_data.Weights         = form.cleaned_data["Weights"]
			assets_server_data.Private_IP      = form.cleaned_data["Private_IP"]
			assets_server_data.Public_IP       = form.cleaned_data["Public_IP"]
			assets_server_data.Admin_IP        = form.cleaned_data["Admin_IP"]
			assets_server_data.SN              = form.cleaned_data["SN"]
			assets_server_data.Response        = form.cleaned_data["Response"]
			assets_server_data.expiration      = form.cleaned_data["expiration"]
			assets_server_data.CPU             = form.cleaned_data["CPU"]
			assets_server_data.CPU_NUM         = form.cleaned_data["CPU_NUM"]
			assets_server_data.MEM             = form.cleaned_data["MEM"]
			assets_server_data.MEM_NUM         = form.cleaned_data["MEM_NUM"]
			assets_server_data.MEM_SINGLE      = form.cleaned_data["MEM_SINGLE"]
			assets_server_data.HDD             = form.cleaned_data["HDD"]
			assets_server_data.HDD_NUM         = form.cleaned_data["HDD_NUM"]
			assets_server_data.HDD_SINGLE      = form.cleaned_data["HDD_SINGLE"]
			assets_server_data.RAID_Type       = form.cleaned_data["RAID_Type"]
			assets_server_data.MAC_1           = form.cleaned_data["MAC_1"]
			assets_server_data.MAC_2           = form.cleaned_data["MAC_2"]
			assets_server_data.MAC_3           = form.cleaned_data["MAC_3"]
			assets_server_data.MAC_4           = form.cleaned_data["MAC_4"]

			if assets_server_data.save() == None:
				return render_to_response('assets_server_add.html',{'form':form,'error':'添加成功！！！','alert':'alert-success'})
			else:
				return render_to_response('assets_server_add.html',{'form':form,'error':'添加失败！！！','alert':'alert-error'})
		else:
			return render_to_response('assets_server_add.html',{'form':form,'error':'添加失败！！！','alert':'alert-error'})
	else:
		form = assets_server_add_Form()
		return render_to_response('assets_server_add.html', {'form':form,'a_path':a_path,'i_user':i_user})

def assets_server_view(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	print id
	return HttpResponse("assets_server_view" + id)

def assets_server_edit(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_server_edit" + id)

def assets_server_delete(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_server_delete" + id)