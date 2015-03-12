#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    level    = models.CharField(max_length=50,default="管理员")
    status   = models.CharField(max_length=50,default="label-success")
    lasttime = models.DateTimeField(auto_now=True)
    allow_ip = models.IPAddressField(default="127.0.0.1")
    photo    = models.ImageField(upload_to="123/",blank=True,null=True,default='NO')
    email    = models.EmailField()

class Assets_Server(models.Model):
    Room            = models.CharField(max_length=50, blank=True)
    System          = models.CharField(max_length=50, blank=True)
    Type            = models.CharField(max_length=50, blank=True)
    Use             = models.TextField()
    Brand           = models.CharField(max_length=50, blank=True)
    Equipment_Model = models.CharField(max_length=50, blank=True)
    Weights         = models.CharField(max_length=50, blank=True)
    Private_IP      = models.IPAddressField()
    Public_IP       = models.IPAddressField()
    Admin_IP        = models.IPAddressField()
    SN              = models.CharField(max_length=50, blank=True)
    Response        = models.CharField(max_length=50, blank=True)
    expiration      = models.CharField(max_length=50, blank=True)
    CPU             = models.CharField(max_length=50, blank=True)
    CPU_NUM         = models.CharField(max_length=50, blank=True)
    MEM             = models.CharField(max_length=50, blank=True)
    MEM_NUM         = models.CharField(max_length=50, blank=True)
    MEM_SINGLE      = models.CharField(max_length=50, blank=True)
    HDD             = models.CharField(max_length=50, blank=True)
    HDD_NUM         = models.CharField(max_length=50, blank=True)
    HDD_SINGLE      = models.CharField(max_length=50, blank=True)
    RAID_Type       = models.CharField(max_length=50, blank=True)
    MAC_1           = models.CharField(max_length=50, blank=True)
    MAC_2           = models.CharField(max_length=50, blank=True)
    MAC_3           = models.CharField(max_length=50, blank=True)
    MAC_4           = models.CharField(max_length=50, blank=True)

class Server(models.Model):
    name      = models.CharField(max_length=50)
    server_ip = models.IPAddressField()
    port      = models.CharField(max_length=50)
    username  = models.CharField(max_length=50)
    password  = models.CharField(max_length=50)

class Log(models.Model):
    name      = models.CharField(max_length=50)
    client_ip = models.IPAddressField()
    date_time = models.DateTimeField(auto_now_add=True)
    command   = models.TextField()
    status    = models.CharField(max_length=2)

class Site(models.Model):
    title       = models.CharField(max_length=50, blank=True)
    reg_status  = models.CharField(max_length=20, blank=True)
    ssh_keygen  = models.TextField(blank=True)
    angent_port = models.CharField(max_length=50, blank=True)
    angent_user = models.CharField(max_length=50, blank=True)
    angent_pass = models.CharField(max_length=50, blank=True)
    mail_snmp   = models.IPAddressField(blank=True)
    mail_port   = models.CharField(max_length=50, blank=True)
    mail_user   = models.CharField(max_length=50, blank=True)
    mail_pass   = models.CharField(max_length=50, blank=True)
    mail_from   = models.EmailField(blank=True)