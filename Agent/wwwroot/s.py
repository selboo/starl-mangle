#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import socket, os, subprocess, sys
import time,select,threading
import rsa,base64
from l_command import *
PRIVATE = os.getcwd()+"/private.pem"

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
    except rsa.pkcs1.DecryptionError, e:
        message = False
        print 'ID-002 DecryptionError...:%s' % e
    return message

def tcpsocket():
    try:
        name =  'selboo'
        listen_ip = '0.0.0.0'
        socket_port = '54321'
        buffer_size = '81920000'
        
        listen_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_tcp.bind((listen_ip, int(socket_port)))
        listen_tcp.listen(10)
    except socket.error, e:
        print 'ID-001 Create Socket Error...:%s' % e
        os._exit(0)

    def command(tag, connection, reault):
        if tag == 1:
            Reault_exchangx = exchengx_text(reault)
            #connection.sendall(base64.encodestring(Reault_exchangx))
            connection.sendall(Reault_exchangx)
            connection.close()
            return 0
        else:
            connection.sendall(reault)
            connection.close()
            return 0
        return 1

    def tcmd(Test, listen_tcp):
        connection,address = listen_tcp.accept()
        infds,outfds,errfds = select.select([connection,],[],[],5) 

        if len(infds) == 0: 
            return 0

        buf_src = connection.recv(int(buffer_size))  
        
        if decryption(buf_src):
            buf = decryption(buf_src)
        else:
            buf_src = 'Decryption failed '+buf_src
            connection.sendall(buf_src)
            buf = ''

        cmd = l_main(buf)
        if cmd:
            command(2, connection, str(cmd))
            return 0

        if len(buf) != 0:
            p = subprocess.Popen(str(buf), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            Result_out = p.stdout.readlines()
            if Result_out:
                command(1, connection, Result_out)

            Result_err = p.stderr.readlines()
            if Result_err:
                command(1, connection, Result_err)

        return 0

    while True:
        infds,outfds,errfds = select.select([listen_tcp,],[],[],5)
        if len(infds) != 0:
            ting = threading.Thread(target=tcmd, args=('Test', listen_tcp))
            ting.start()

def createDaemon():
    try:
        if os.fork() > 0:
            os._exit(0)
    except OSError, error:
        print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)
     
    os.chdir('/')
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            #print 'Daemon PID %d' % pid
            os._exit(0)
    except OSError, error:
        print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)
    funzioneDemo() 

def funzioneDemo():
    tcpsocket()

if __name__ == '__main__':
    createDaemon()

