import socket
import select
import Queue

server=('0.0.0.0', 12345)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setblocking(False)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(server)
sock.listen(10)

#conn,addr = sock.accept()

rlists = [sock]
wlists = []

msg_que={}
timeout=20

a = '''

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  19224   532 ?        Ss   Aug16   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Aug16   0:00 [kthreadd]
'''

#print 'ccc: ', addr,conn
while rlists:
	rs,ws,es = select.select(rlists,wlists,rlists,timeout)
	if not (rs or ws or es):
		print 'timeout 20 '
		#break
		continue
	for s in rs:
		print '----------- rs -----------'
		print s
		print '----------- rs -----------'
		if s is sock:
			conn,addr = s.accept()
			print 'client ', addr,conn
			conn.setblocking(False)
			rlists.append(conn)
			msg_que[conn]=Queue.Queue()
		else:
			data = s.recv(1024)
			if data:
				print '11111 ', data
				msg_que[s].put(data)
				if s not in wlists:
					wlists.append(s)
			else:
				if s in wlists:
					wlists.remove(s)
				rlists.remove(s)
				s.close()
				del msg_que[s]

	for s in ws:
		print '----------- ws -----------'
		print s
		print '----------- ws -----------'
		try:
			msg = msg_que[s].get_nowait()
		except Queue.Empty:
			print '2222 msg empty'
			wlists.remove(s)
		except KeyError:
			print '444444444444'
		else:
			s.send(a)


	for s in es:
		print '----------- es -----------'
		print s
		print '----------- es -----------'
		print '33333333', s.getpeername()
		if s in rlists:
			rlists.remove(s)
		if s in wlists:
			wlists.remove(s)
		s.close()
		del msg_que[s]
#sock.close()



