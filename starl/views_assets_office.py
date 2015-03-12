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

def assets_office(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_office")

def assets_office_add(request):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_office_add")

def assets_office_view(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_office_view" + id)

def assets_office_edit(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_office_edit" + id)

def assets_office_delete(request, id):
	if status(request) == 1:
		return render_to_response('login.html',{'error':'链接超时，请重新登陆！！!','alert':'alert-error'})

	return HttpResponse("assets_office_delete", id)

