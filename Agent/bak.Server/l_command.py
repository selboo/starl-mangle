#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8

import os,sys
import httplib2,hashlib
http = httplib2.Http()

def l_main(cmd):
	if cmd == 'l_version'	:return l_version()
	if cmd == 'l_update'	:return l_update()
	if cmd == 'l_pwd'		:return l_pwd()
	return False

def l_pwd():
	return sys.path[0]

def l_version():
	return '0.1'

def file_md5(filename):
	f = open(filename, 'a+r')
	return hashlib.md5(f.read()).hexdigest()

def file_write(filename, up_path):
	url = 'http://agent.mangle.starl.com.cn/'+filename
	f   = open (up_path, 'w')
	f.write(get_http(url))
	return 1

def get_http(url):
	response,content = http.request(url,'GET')
	return content

def l_update():
	update_url  = 'http://agent.mangle.starl.com.cn/update.txt'
	content     = get_http(update_url)
	update_dict = eval(content)
	update_done = {}
	if update_dict.get('version') == l_version():
		return 'latest'
	else:
		del update_dict['version']

	for up_name, up_md5 in update_dict.items():
		up_path = sys.path[0] + '/' + up_name
		local_file_md5 = file_md5(up_path)
		serve_file_md5 = up_md5
		if local_file_md5 != serve_file_md5:
			if file_write(up_name, up_path):
				update_done[up_name] = 'update ok...'
			else:
				update_done[up_name] = 'update no...'

	if update_done:
		return update_done
	else:
		return 'All latest...'
