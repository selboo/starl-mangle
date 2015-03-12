#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import sys,os,optparse,socket,time
import rsa,base64
PUBLIC = os.getcwd()+"/public.pem"

def usage():
        help_msg = '''
        --host                   remote ip or host
        --port                   remote tcp port
        --command                remote exec command
        '''
        print help_msg
        print "user command:\n\t%s --host 192.168.1.126 --port 65501 --command \"netstat -an\" " %sys.argv[0]

def key():
    return 'Selboo'

def encryption(cmd):
    with open(PUBLIC) as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
    return rsa.encrypt(cmd, pubkey)

def remote_exec(host, port, command):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
    except socket.error, arg:
        errno, err_msg = arg
        print "Connect server failed: %s, errno=%d" % (err_msg, errno)
    #print command
    sock.sendall(command)
    data = sock.recv(81920000)
    #print data
    #data = base64.decodestring(data)
    sock.close()
    return data

def main():
        opt = optparse.OptionParser()
        opt.add_option('--host')
        opt.add_option('--port',default = 65501)
        opt.add_option('--command')
        options, arguments = opt.parse_args()

        def debug_info():
                print 'host:\t',        options.host
                print 'port:\t',        options.port
                print 'command:\t',      options.command

        if not (options.host and options.command):
                usage()
                sys.exit(1)
        print remote_exec(options.host, options.port, options.command)
        
if __name__ == '__main__':
        main()
        
