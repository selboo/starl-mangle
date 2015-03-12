#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.forms import ModelForm
from django import forms

class switch_Form(forms.Form):
	name      = forms.CharField(label = '名字')
	switch_ip = forms.CharField(label = 'IP')
	sw_type   = forms.CharField(label = '设备')
	model     = forms.CharField(label = '型号')
	speed     = forms.CharField(label = '速度')
	post      = forms.CharField(label = '端口数')

class switch_add_Form(forms.Form):
	name      = forms.CharField(label = '名字')
	switch_ip = forms.CharField(label = 'IP')
	user      = forms.CharField(label = '用户名')
	password  = forms.CharField(label = '链接密码')
	enable    = forms.CharField(label = 'en密码')
	sw_type   = forms.CharField(label = '设备')
	model     = forms.CharField(label = '型号')
	speed     = forms.CharField(label = '速度')
	post      = forms.CharField(label = '端口数')

class monitor_Form(forms.Form):
	ip             = forms.CharField(label = 'IP')
	datatime       = forms.CharField(label = '时间')
	traffic_input  = forms.CharField(label = '下行带宽')
	traffic_output = forms.CharField(label = '上行带宽')
	packets_input  = forms.CharField(label = '下行数据包')
	packets_output = forms.CharField(label = '上行数据包')

class Switch_bonding(forms.Form):
	step           = forms.CharField(required=False)
	name           = forms.CharField(required=False)
	ip             = forms.CharField(required=False)
	post           = forms.CharField(required=False)
	int_status     = forms.CharField(required=False)
	int_post       = forms.CharField(required=False)
	int_vlan       = forms.CharField(required=False)
	switch_db_name = forms.CharField(required=False)
	switch_bd_post = forms.CharField(required=False)
	switch_bd_vlan = forms.CharField(required=False)
	switch_bd_mac  = forms.CharField(required=False)
	switch_bd_ip   = forms.CharField(required=False)


