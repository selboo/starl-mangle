#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context, RequestContext
from django.core.mail import send_mail
from django.conf import settings

from starl.forms import *
from starl.models import *
from starl.views import *
from starl.smail import *
from forms import *

import re,datetime,time,Image

def user(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'用户管理'
	i_user = request.COOKIES.get('starl', '')

	user_form = user_Form()
	form = User.objects.filter()
	return render_to_response('user.html', {'user_form':user_form,'form':form,'a_path':a_path,'i_user':i_user})

def user_add(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'添加用户'
	i_user = request.COOKIES.get('starl', '')

	if request.method == 'POST':
		form = user_add_Form(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			level    = form.cleaned_data['level']
			email    = form.cleaned_data['email']
			u_status = form.cleaned_data['u_status']

			chack_username = User.objects.filter(username=username).count()

			if chack_username != 0:
				return render_to_response('user_add.html',{'form':form,'error':'用户名已存在！！！','alert':'alert-error'})
			
			imgfile = username
			if 'photo' in request.FILES:
				imgfl = settings.IMG_ROOT+imgfile+".jpeg"
				imgfe = request.FILES['photo']
				image = Image.open(imgfe)
				image.thumbnail((55,55), Image.ANTIALIAS)
				image.save(imgfl, "jpeg") 
				photo = settings.IMG_PATH+imgfile+".jpeg"
			else:
				photo = "NO"

			if check_email(email) == 0:
				return render_to_response('user_add.html',{'form':form,'error':'邮件格式错误！！！','alert':'alert-error'})
			else:
				if u_status == u'开启':
					u_status = 'label-success'
				else:
					u_status = ''
				password = md5sum(password, 3)
				User.objects.create(username=username,
									password=password,
									email=email,
									level=level,
									status=u_status,
									photo=photo)
				return HttpResponseRedirect("/user/")
		else:
			return render_to_response('user_add.html',{'form':form,'error':'添加失败！！！','alert':'alert-error'})
	else:
		form = user_add_Form()
		return render_to_response('user_add.html', {'form':form,'a_path':a_path,'i_user':i_user})

def user_view(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'用户管理'
	i_user = request.COOKIES.get('starl', '')

	user_form = user_add_Form()
	if id >= u'\u0030' and id<=u'\u0039': # 判断id是 整形 还是 字符串
		form = User.objects.filter(id=id)
	else:
		form = User.objects.filter(username=id)

	return render_to_response('user.html', {'user_form':user_form,'form':form,'a_path':a_path,'i_user':i_user})

def user_edit(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'用户编辑'
	i_user = request.COOKIES.get('starl', '')

	if request.method == 'POST':
		user_form = user_edit_Form(request.POST, request.FILES)
		if user_form.is_valid():
			password = user_form.cleaned_data['password']
			level    = user_form.cleaned_data['level']
			email    = user_form.cleaned_data['email']
			allow_ip = user_form.cleaned_data['allow_ip']
			u_status = user_form.cleaned_data['u_status']

			user = User.objects.get(id=id)

			imgfile = user.username
			if 'photo' in request.FILES:
				imgfl = settings.IMG_ROOT+imgfile+".jpeg"
				imgfe = request.FILES['photo']
				image = Image.open(imgfe)
				image.thumbnail((55,55), Image.ANTIALIAS)
				image.save(imgfl, "jpeg") 
				user.photo = settings.IMG_PATH+imgfile+".jpeg"
			
			if password != "":
				user.password = md5sum(password, 3)
			user.level    = level
			user.email    = email
			user.allow_ip = allow_ip 
			if u_status == u'开启':
				user.status = 'label-success'
			else:
				user.status = ''
			form = User.objects.filter(id=id)
			if user.save() == None:
				return render_to_response('user_edit.html',{'user_form':user_form,'form':form,'error':'修改成功！！！','alert':'alert-success','a_path':a_path,'i_user':i_user})
			else:
				return render_to_response('user_edit.html',{'user_form':user_form,'form':form,'error':'修改失败！！！','alert':'alert-error','a_path':a_path,'i_user':i_user})

		else:
			return render_to_response('user_edit.html',{'form':form,'error':'修改失败！！！','alert':'alert-error'})
	else:
		user_form = user_edit_Form()
		form = User.objects.filter(id=id)
		return render_to_response('user_edit.html', {'user_form':user_form,'form':form,'a_path':a_path,'i_user':i_user})

def user_delete(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})
	a_path = u'用户管理'
	i_user = request.COOKIES.get('starl', '')

	user_form = user_Form()
	form = User.objects.filter()
	user = User.objects.get(id=id)
	user.delete()
	return render_to_response('user.html', {'user_form':user_form,'form':form,'i_user':i_user,'a_path':a_path,'error':'删除成功！！！','alert':'alert-success'})
