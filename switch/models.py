#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.db import models

class Switch(models.Model):
	name      = models.CharField(max_length='50')
	switch_ip = models.CharField(max_length='50')
	user      = models.CharField(max_length='50',default='mima')
	password  = models.CharField(max_length='50',default='mima')
	enable    = models.CharField(max_length='50',default='mima')
	sw_type   = models.CharField(max_length='50',default='route') # route or switch
	model     = models.CharField(max_length='50',default='2960')  # 2960 or 3750
	speed     = models.CharField(max_length='50',default='100M')  # 100M or 1000M
	post      = models.CharField(max_length='50',default='24')    # 24 or 48

class Monitor(models.Model):
	ip             = models.IPAddressField()
	datatime       = models.DateTimeField()
	traffic_input  = models.CharField(max_length='20',default='mima')
	traffic_output = models.CharField(max_length='20',default='mima')
	packets_input  = models.CharField(max_length='20',default='mima')
	packets_output = models.CharField(max_length='20',default='mima')
	ping_min       = models.CharField(max_length='20',default='mima')
	ping_avg       = models.CharField(max_length='20',default='mima')
	ping_max       = models.CharField(max_length='20',default='mima')


