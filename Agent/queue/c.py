import socket

server('192.168.80.250', 12346)
msg = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server)

for m in msg:
	sock.send(m)

sock.close()















