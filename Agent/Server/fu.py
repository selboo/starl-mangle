#coding=gb2312
import socket, os, subprocess, sys
import time, select, thread, SocketServer

def key():
    return 'Selboo'

def tcpsocket():
    
    name = 'Selboo'
    listen_ip = '127.0.0.1'
    socket_port = '65501'
    buffer_size = '1024'

    listen_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    listen_tcp.bind((listen_ip, int(socket_port)))
    listen_tcp.listen(10)
    
    
    while True:
        connection,addres = listen_tcp.accept()
        buf = connection.recv(int(buffer_size))
        print "while"
        if len(buf) != 0:
            p = subprocess.Popen(str(buf), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
            Result_out = p.stdout.readlines()
            Reault_out_exchangx = exchengx_text(Result_out)
            connection.send(Reault_out_exchangx)
                    
            Result_err = p.stderr.readlines()
            Result_err_exchangx = exchengx_text(Result_err)
            connection.send(Result_err_exchangx)
        print "%s %s" %(addres,buf)
        
if __name__ == '__main__':
    tcpsocket()

    