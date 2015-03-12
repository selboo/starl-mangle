#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8

import time
import random
import httplib2
import random
import thread
import threading
import optparse,sys


http = httplib2.Http(timeout=10)

headers={"Accept-Encoding": "gzip, deflate",
        "cache-control":"no-cache"}

def create_adder():
        init = [0]
        def add(x):
                init[0] += x
                return init[0]
        return add
Su = create_adder()
Fa = create_adder()

def Get_URL(K, V):
        try:
                URL = "http://www.herosrise.com/Common/Interface/TempHeroRisinig.aspx?name=%s&value=%s" %(K,V)
                response,content = http.request(URL,'GET')
        except Exception:
        	return "Failsh Timeout"
        
	return content

def Thread_URL(c,n):

        for i in range(0,n):
                Random_K = random.random()
                Random_V = random.random()

                time.sleep(0.01)
                s = Get_URL(Random_K, Random_V)
                print c,i,time.time(),s
                if s == "Success":
                        Su(1)
                else:
                        Fa(1)

def t(c,n):
        for i in range(0,n):
        	print c,i
                
def usage():
    help_msg = '''
    Options are:
        -n requests     Number of requests to perform
        -c concurrency  Number of multiple requests to make   
    '''
    print "\t%s -c 10 -n 100 " %sys.argv[0] 
    print help_msg
    
if __name__ == '__main__':

    opt = optparse.OptionParser()
    opt.add_option('-n','--requests')
    opt.add_option('-c','--concurrency')
    options, arguments = opt.parse_args()
    
    if not (options.requests):
        usage()
        sys.exit(1)

    threads = []
    n = int(options.requests)
    c = int(options.concurrency)
        
    for i in range(0, c):
        thread = threading.Thread(target=Thread_URL,args=(i,n))
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
    print "Success",Su(0)
    print "Failure",Fa(0)

