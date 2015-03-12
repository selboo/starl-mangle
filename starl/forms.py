#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.forms import ModelForm
from django import forms


class Reg_Form(forms.Form):
	username  = forms.CharField(label = 'icon-user', widget=forms.TextInput(attrs={'class':'span12'}))
	password  = forms.CharField(label = 'icon-locked', widget=forms.PasswordInput(attrs={'class':'span12'}))
	password2 = forms.CharField(label = 'icon-locked', widget=forms.PasswordInput(attrs={'class':'span12'}))
	email     = forms.CharField(label = 'icon-envelope-closed', widget=forms.TextInput(attrs={'class':'span12'}))

class login_Form(forms.Form):
	username = forms.CharField(label = '用户', max_length = 50, widget=forms.TextInput(attrs={'class':'span12'}))
	password = forms.CharField(label = '密码', widget=forms.PasswordInput(attrs={'class':'span12'}))

class user_Form(forms.Form):
    username = forms.CharField(label = '用户名')
    level    = forms.CharField(label = '权限')
    email    = forms.CharField(label = '邮件')
    lasttime = forms.CharField(label = '最后登陆时间')
    allow_ip = forms.CharField(label = '允许IP')

class user_add_Form(forms.Form):
    username = forms.CharField(label = '用户名')
    password = forms.CharField(label = '密码')
    level    = forms.CharField(label = '权限')
    email    = forms.CharField(label = '邮件')
    u_status = forms.CharField(label = '状态')
    photo    = forms.ImageField(label = '头像', required=False)

class user_edit_Form(forms.Form):
    username = forms.CharField(label = '用户名', required=False)
    password = forms.CharField(label = '密码', required=False)
    level    = forms.CharField(label = '权限')
    email    = forms.CharField(label = '邮件')
    allow_ip = forms.CharField(label = '允许IP')
    u_status = forms.CharField(label = '状态')
    photo    = forms.ImageField(label = '头像', required=False)

class assets_server_add_Form(forms.Form):
    Room            = forms.CharField(label='位置', required=False)
    System          = forms.CharField(label='系统', required=False)
    Type            = forms.CharField(label='使用人', required=False)
    Use             = forms.CharField(label='说明', required=False)
    Brand           = forms.CharField(label='品牌', required=False)
    Equipment_Model = forms.CharField(label='型号', required=False)
    Weights         = forms.CharField(label='权重', required=False)
    Private_IP      = forms.CharField(label='内网IP', required=False)
    Public_IP       = forms.CharField(label='外网IP', required=False)
    Admin_IP        = forms.CharField(label='管理IP', required=False)
    SN              = forms.CharField(label='SN', required=False)
    Response        = forms.CharField(label='售后类型', required=False)
    expiration      = forms.CharField(label='过保时间', required=False)
    CPU             = forms.CharField(label='CPU型号', required=False)
    CPU_NUM         = forms.CharField(label='CPU核数', required=False)
    MEM             = forms.CharField(label='内存', required=False)
    MEM_NUM         = forms.CharField(label='内存条数', required=False)
    MEM_SINGLE      = forms.CharField(label='内存单条', required=False)
    HDD             = forms.CharField(label='硬盘', required=False)
    HDD_NUM         = forms.CharField(label='硬盘数量', required=False)
    HDD_SINGLE      = forms.CharField(label='硬盘单块', required=False)
    RAID_Type       = forms.CharField(label='RAID', required=False)
    MAC_1           = forms.CharField(label='MAC_1', required=False)
    MAC_2           = forms.CharField(label='MAC_2', required=False)
    MAC_3           = forms.CharField(label='MAC_3', required=False)
    MAC_4           = forms.CharField(label='MAC_4', required=False)

class site_Form(forms.Form):
    title       = forms.CharField(label = '站点名称', required=False)
    reg_status  = forms.CharField(label = '开放注册', required=False)
    ssh_keygen  = forms.CharField(label = 'SSH密钥', required=False)
    angent_port = forms.CharField(label = 'Agent 端口', required=False)
    angent_user = forms.CharField(label = 'Agent 用户', required=False)
    angent_pass = forms.CharField(label = 'Agent 密码', required=False)
    mail_snmp   = forms.CharField(label = 'SNMP 地址', required=False)
    mail_port   = forms.CharField(label = 'SNMP 端口', required=False)
    mail_user   = forms.CharField(label = 'SNMP 用户', required=False)
    mail_pass   = forms.CharField(label = 'SNMP 密码', required=False)
    mail_from   = forms.CharField(label = '收件人', required=False)