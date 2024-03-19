import socket
from struct import pack, unpack, calcsize

HOST = '192.168.0.4' 
PORT = 12345
test = []

# Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print ('****connecting success****')
print ('if you want to close quit the comunication, you can write "quit".')

while True:
	command = input(':')
	s.send('connected')
	reply = s.recv(1024)
	if reply == 'Terminate':
		break

	test = []
	for i in (reply):
		test.append(i)

	print(test)
	print (unpack('b', test[0]))