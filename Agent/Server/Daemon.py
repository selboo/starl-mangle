#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8

import sys, os, time, atexit
from signal import SIGTERM
import time
import os
from multiprocessing import Process, Pipe
import socket, os, subprocess, sys
import time, select, thread, SocketServer
import s

class Daemon:
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """
    def __init__(self, pidfile='p.txt', stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write("%s\n" % pid)

    def delpid(self):
        pass
        #os.remove(self.pidfile)

    def getpid(self):
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        return pid

    def start(self, conn):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        
        # Start the daemon
        self.daemonize()
        self.run(conn)

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            pf = file('/p.txt','r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print str(err)
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self, conn):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """
        conn.send(os.getpid())
        conn.close()
        tcpsocket()

def exchengx_text(text):
    Result_Text = []
    for i in range(len(text)):
        Result_Text.append(''.join(text[i]))
    Result_Text = ''.join(Result_Text)    
    return Result_Text

def tcpsocket():
    
    name = 'Selboo'
    listen_ip = '0.0.0.0'
    socket_port = '54321'
    buffer_size = '1024'

    listen_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    listen_tcp.bind((listen_ip, int(socket_port)))
    listen_tcp.listen(10)
    print 'D', os.getppid()
    print 'D', os.getpid()
    
    while True:
        connection,addres = listen_tcp.accept()
        buf = connection.recv(int(buffer_size))
        print "while"
        command = str(buf)
        buf = restart(command)
        if len(buf) != 0:
            p = subprocess.Popen(str(buf), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
            Result_out = p.stdout.readlines()
            Reault_out_exchangx = exchengx_text(Result_out)
            connection.send(Reault_out_exchangx)
                    
            Result_err = p.stderr.readlines()
            Result_err_exchangx = exchengx_text(Result_err)
            connection.send(Result_err_exchangx)
        print "%s %s" %(addres,buf)
        
def restart(command):

    if command == 'l_restart':
        #import s
        #s.createDaemon()
        print 'pid_S:',pid_S
        l = 'echo Restart... %s' %(pid_S)
        os.kill(pid_S, SIGTERM)
        start_S()
        return l
    return command

def start_S():
    global pid_S
    parent_conn_S, child_conn_S = Pipe()

    p_S = Process(target=s.createDaemon, args=(child_conn_S,))
    p_S.start()
    p_S.join()
    pid_S = parent_conn_S.recv()

def start_D():
    global pid_D
    parent_conn_D, child_conn_D = Pipe()

    a = Daemon()
    p_D = Process(target=a.start, args=(child_conn_D,))
    p_D.start()
    p_D.join()
    pid_D = parent_conn_D.recv()

if __name__ == '__main__':
    start_S()
    start_D()

    print 'pid_S:',pid_S
    print 'pid_D:',pid_D

