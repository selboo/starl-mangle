#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context, RequestContext
from django.core.mail import send_mail
from django.contrib.sessions.models import Session

from starl.forms import *
from starl.models import *
from switch.models import *
from forms import *

import re,datetime,time
import hashlib
import IPy

def status(request):
	cookies_username = request.COOKIES.get('starl', '')
	session_username = request.session.get('starl')
	if cookies_username == "" or session_username == None:
		return 1
	else:
		return 0

def api_session(request, api_s):
	ret_s = ""
	if len(api_s) != 32:
		return HttpResponse('Session Error...')

	chack_session = Session.objects.filter(session_key=api_s).count()
	if chack_session > 0:
		s = Session.objects.get(pk=api_s)
		if not s.get_decoded():
			ret_s = "Session Null..."
		elif len(s.get_decoded()['starl']) > 0:
			ret_s = "ok"
	else:
		ret_s = "No Session..."

	return HttpResponse(ret_s)

def default(request):
	if status(request) == 1:
		return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/index/")

def index(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	User_Num = User.objects.filter().count()
	Swit_Num = Switch.objects.filter().count()
	Serv_Num = 28
	Warn_Num = 219

	User_Num_New = 1
	Swit_Num_New = 4
	Serv_Num_New = 3
	Warn_Num_New = 12

	user_data = User.objects.filter()
	onedate   = str(datetime.datetime.now() - datetime.timedelta(hours=1))[0:19]
	swit_data = Monitor.objects.filter(datatime__gte=onedate)

	i_user = request.COOKIES.get('starl', '')
	return render_to_response('index.html',{'swit_data':swit_data,'user_data':user_data,'User_Num_New':User_Num_New,'Swit_Num_New':Swit_Num_New,'Serv_Num_New':Serv_Num_New,'Warn_Num_New':Warn_Num_New,'User_Num':User_Num,'Swit_Num':Swit_Num,'Serv_Num':Serv_Num,'Warn_Num':Warn_Num,'i_user':i_user})

def login(request):
	print "32333";
	if request.method == 'POST':
		print 'post';
		form = login_Form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			password = md5sum(password, 3)
			login = User.objects.filter(username=username,password=password,status='label-success')

			s_us = User.objects.get(username=username).status
			s_ip = User.objects.get(username=username).allow_ip
			c_ip = request.META['REMOTE_ADDR']
			f_ip = c_ip in IPy.IP(s_ip)
			if login and f_ip:
				response = HttpResponseRedirect("/index/")
				response.set_cookie('starl', username, 86400)
				request.session['starl'] = username
				request.session.set_expiry(3600)


				ltime = User.objects.get(username=username)
				ltime.lasttime = str(datetime.datetime.now())[0:19]
				ltime.save()

				return response
			else:
				if s_us != 'label-success':
					error = '用户名已禁用！！！'
					return render_to_response('login.html',{'form':form,'error':error,'alert':'alert-error'})
				elif f_ip == False:
					error = '您所在IP禁止登陆！！！'
					return render_to_response('login.html',{'form':form,'error':error,'alert':'alert-error'})
				else:
					error = '用户名或密码错误！！！'
					return render_to_response('login.html',{'form':form,'error':error,'alert':'alert-error'})
		else:
			return HttpResponseRedirect("/login/")
	else:
		form = login_Form()
		alert = "alert-info"
		if Site.objects.get(id=1).reg_status == "on":
			reg_status = "on"
		else:
			reg_status = "off"
		return render_to_response('login.html',{'form':form,'alert':alert,'reg_status':reg_status})

def logout(request):
	del request.session['starl']
	response = HttpResponseRedirect("/login/")
	response.delete_cookie('starl')
	return render_to_response('login.html',{'error':'退出成功！！!'})

def logoutS(request):
	del request.session['starl']
	return HttpResponse('退出成功S')

def logoutC(request):
	response = HttpResponse('退出成功C')
	response.delete_cookie('starl')
	return response

def reg(request):
	if request.method == 'POST':
		form = Reg_Form(request.POST)
		if form.is_valid():
			username  = form.cleaned_data['username']
			password  = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			#level    = form.cleaned_data['level']
			email     = form.cleaned_data['email']

			chack_username = User.objects.filter(username=username).count()

			if Site.objects.get(id=1).reg_status != "on":
				return render_to_response('reg.html',{'form':form,'error':"系统关闭注册！！！",'alert':"alert-error"})

			elif chack_username != 0:
				alert = "alert-error"
				error = "用户名已存在！！！" 
				return render_to_response('reg.html',{'form':form,'error':error,'alert':alert})
			elif password != password2:
				error = "两次密码不匹配！！！"
				alert = "alert-error"
				return render_to_response('reg.html',{'form':form,'error':error,'alert':alert})
			elif check_email(email) == 0:
				error = "邮件格式错误！！！"
				alert = "alert-error"
				return render_to_response('reg.html',{'form':form,'error':error,'alert':alert})
			else:
				password = md5sum(password, 3)
				User.objects.create(username=username,password=password,email=email)
				return render_to_response('login.html',{'error':'注册成功，请登录！！!','alert':'alert-success'})
		else:
			alert = "alert-error"
			error = "输入错误"
			return render_to_response('reg.html',{'form':form,'error':error,'alert':alert})
	else:
		form = Reg_Form()
		alert = "alert-info"
		if Site.objects.get(id=1).reg_status == "on":
			return render_to_response('reg.html',{'form':form,'alert':alert})
		else:
			return render_to_response('login.html',{'error':'禁止注册！！!','alert':'alert-error'})
		
def check_email(email):
	address_email  = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
	if address_email.search(email):
		return 1
	else:
		return 0

def hello(request):
	if 'q' in request.GET:
		q_ver = request.GET['q'].encode('utf-8')
		message = 'You input for 暗示法 = %r' % q_ver
		print q_ver
		return HttpResponse(message)
	if 'lista' in request.GET:
		l1 = Publisher.objects.all()
		return render_to_response('hello.html', {'l1': l1})
	if 'listb' in request.GET:
		l1 = Publisher.objects.all()
		f = AuthorForm()
		return render_to_response('hellob.html', {'l1': l1,'f':f})
	#return HttpResponse("Hello world")

def index_temp_file(request,color,lista):
	return render_to_response('index_temp_file.html', {'color':color, 'lista':lista})

def index_temp(request,input_name):
	t = Template('My name is {{ name }}.')
	c = Context({'name': input_name})
	return HttpResponse(t.render(c))

def index_temp_color(request,input_name,color):
	t = Template('My name is<font color =#{{color}}> {{ name }}.</font>')
	c = Context({'name': input_name,'color':color})
	return HttpResponse(t.render(c))


def current_time(request,string,offset):
	print offset,string
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
         
	dt = datetime.datetime.now()
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def md5sum(password, num=3):
	for i in range(0, num):
		md5pass = hashlib.md5()
		md5pass.update(password)
		password = md5pass.hexdigest()
	return password