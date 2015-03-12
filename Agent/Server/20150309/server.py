#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import socket, os, sys, subprocess
sys.path.insert(0, 'pack/rsa.zip')
sys.path.insert(0, 'pack/pyasn1.zip')
import time,select,threading
import rsa,base64
PRIVATE = os.getcwd()+"/key/private.pem"

def exchengx_text(text):
	Result_Text = []
	for i in range(len(text)):
		Result_Text.append(''.join(text[i]))
	Result_Text = ''.join(Result_Text)	
	return Result_Text

def key():
	return 'Selboo'

def decryption(crypto):
	with open(PRIVATE) as privatefile:
		p = privatefile.read()
		privkey = rsa.PrivateKey.load_pkcs1(p)
	try:
		message = rsa.decrypt(crypto, privkey)
	except:
		message = False
		print 'ID-002 DecryptionError'
	return message

class tcpsocket():
	def __init__(self):
		try:
			self.name		= 'selboo'
			self.listen_ip   = '0.0.0.0'
			self.socket_port = '54321'
			self.buffer_size = '1024'
			
			self.listen_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.listen_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.listen_tcp.bind((self.listen_ip, int(self.socket_port)))
			self.listen_tcp.setblocking(0)
			self.listen_tcp.listen(100)
		except socket.error, e:
			print 'ID-001 Create Socket Error...:%s' % e
			os._exit(0)

	def listen(self):
		return self.listen_tcp

	def tcp_send(self, connection, content):
		tcp_limit  = 100
		tcp_length = len(content)
		tcp_subcon = tcp_length / tcp_limit
		tcp_tail   = tcp_length % tcp_limit

		tcp_start = 0
		tcp_stop  = tcp_limit

		tcp_head = str(tcp_length)+','+str(tcp_subcon)+'|'+self.name
		tcp_head = tcp_head.ljust(tcp_limit)
		connection.send(tcp_head)

		if tcp_length <= tcp_limit:
			connection.send(content[tcp_start:tcp_length])
			return 0

		alist = []
		for i in range(0,tcp_subcon):
			tcp_d = content[tcp_start:tcp_stop]
			connection.send(tcp_d)
			time.sleep(0.0001)
			tcp_start = tcp_stop
			tcp_stop  = tcp_stop + tcp_limit
		tcp_t = content[tcp_start:tcp_length]
		connection.send(tcp_t)
		return 0

	def command(self, tag, connection, reault):
		if tag == 1:
			Reault_exchangx = exchengx_text(reault)
			#connection.send(base64.encodestring(Reault_exchangx))
			#print Reault_exchangx
			self.tcp_send(connection, Reault_exchangx)
			return 0
		else:
			self.tcp_send(connection, reault)
			return 0
		return 1

	def tcmd(self, Test, listen_tcp):
		connection,address = listen_tcp.accept()
		buf_src = connection.recv(int(self.buffer_size))
		buf	 = decryption(buf_src)
		if not buf:
			buf_src = 'Decryption failed '+ buf_src
			self.command(0, connection, buf_src)
			return 0

		if len(buf) != 0:
			p = subprocess.Popen(str(buf), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			Result_out = p.stdout.readlines()
			if Result_out: self.command(1, connection, Result_out)

			Result_err = p.stderr.readlines()
			if Result_err: self.command(1, connection, Result_err)

		connection.close()
		return 0

def start():
	server   = tcpsocket()
	listen_tcp = server.listen()

	while True:
		infds,outfds,errfds = select.select([listen_tcp,],[],[],5)
		if len(infds) != 0:
			ting = threading.Thread(target=server.tcmd, args=('Test', listen_tcp))
			ting.start()
