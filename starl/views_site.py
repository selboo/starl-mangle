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

def site(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'站点设置'
	i_user = request.COOKIES.get('starl', '')
	formdb = Site.objects.filter(id=1)


	if request.method == 'POST':
		form = site_Form(request.POST)
		if form.is_valid():
			title       = form.cleaned_data['title']
			reg_status  = form.cleaned_data['reg_status']
			ssh_keygen  = form.cleaned_data['ssh_keygen']
			angent_port = form.cleaned_data['angent_port']
			angent_user = form.cleaned_data['angent_user']
			angent_pass = form.cleaned_data['angent_pass']
			mail_snmp   = form.cleaned_data['mail_snmp']
			mail_port   = form.cleaned_data['mail_port']
			mail_user   = form.cleaned_data['mail_user']
			mail_pass   = form.cleaned_data['mail_pass']
			mail_from   = form.cleaned_data['mail_from']

			sitedb = Site.objects.get(id=1)
			sitedb.reg_status  = reg_status
			if title       != "": sitedb.title       = title
			if ssh_keygen  != "": sitedb.ssh_keygen  = ssh_keygen
			if angent_port != "": sitedb.angent_port = angent_port
			if angent_user != "": sitedb.angent_user = angent_user
			if angent_pass != "": sitedb.angent_pass = angent_pass
			if mail_snmp   != "": sitedb.mail_snmp   = mail_snmp
			if mail_port   != "": sitedb.mail_port   = mail_port
			if mail_user   != "": sitedb.mail_user   = mail_user
			if mail_pass   != "": sitedb.mail_pass   = mail_pass
			if mail_from   != "": sitedb.mail_from   = mail_from
			print reg_status
			if sitedb.save() == None:
				return render_to_response('site.html',{'formdb':formdb,'form':form,'error':'修改成功！！！','alert':'alert-success','a_path':a_path,'i_user':i_user})
			else:
				return render_to_response('site.html',{'formdb':formdb,'form':form,'error':'修改失败！！！','alert':'alert-error','a_path':a_path,'i_user':i_user})
	else:
		form = site_Form()
		return render_to_response('site.html',{'formdb':formdb,'form':form,'i_user':i_user,'a_path':a_path})

