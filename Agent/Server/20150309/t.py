#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import sys,os,optparse,socket,time,base64
sys.path.insert(0, 'pack/rsa.zip')
sys.path.insert(0, 'pack/pyasn1.zip')
import rsa
PUBLIC = os.getcwd()+"/key/public.pem"
PRIVATE = os.getcwd()+"/key/private.pem"

def encryption(cmd):
    with open(PUBLIC) as publickfile:
        p = publickfile.read()
        try:
            pubkey  = rsa.PublicKey.load_pkcs1(p)
            message = rsa.encrypt(cmd, pubkey)
        except:
            message = "Add encryption False"
            print "Add encryption False"
            os._exit(0)
    return message





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

a = encryption('id')


print decryption(a)
