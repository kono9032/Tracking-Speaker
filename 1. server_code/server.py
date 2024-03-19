#blid error -> netstate -an -o, taskkill /f /pid 1234

import socket
import time
import threading
from struct import *

#HOST = '172.30.1.14'
HOST = '192.168.0.4'
PORT = 12345

all_data_combine = {"personNumber":0, "callNumber":[]}
#{personNumber:0 , callNumber:[123,x,y, 124,x,y, ...]}

def make_send_value(callNumber):
	val = []
	if (not(callNumber)): #if no callNumber, just send personNumber.
		val.append(all_data_combine["personNumber"])
		send_value = pack('HHHH', val[0],0,0,0)
	else: #send all requested data.
		val.append(all_data_combine["personNumber"])
		n = all_data_combine["callNumber"].index(callNumber)
		for i in range (3):
			val.append(all_data_combine["callNumber"][n+i])
		send_value = pack('HHHH', val[0], val[1], val[2], val[3])
	return send_value

class comunicateProgram():
	s = None
	(conn, addr) = None, None

	def send_personNumber(self):
		reply = make_send_value(0)
		print("did")
		self.conn.send(reply)

	def socket_comunity_thread(self):
		# create new socket -----------------------------------------------
		while True:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print("socket created")
			self.s.settimeout(None)
			self.s.bind((HOST, PORT))
			self.s.listen()
			print ('Socket awaiting messages')
			(self.conn, self.addr) = self.s.accept()
			print ('Connected :', self.conn, self.addr)
			# comunicate with client --------------------------------------
			while True:
				try:
					data = self.conn.recv(1024)
					print ('From client------- : ' + data.decode())
					reply = ''
		
					if data.decode() == 'connected':
						reply = make_send_value(0)
						self.conn.send(reply)
						print("To client--------- : ",reply)

					elif data.decode() == 'call':
						if (all_data_combine["personNumber"] != 0):
							all_data_combine["personNumber"] -= 1
							reply = make_send_value(all_data_combine["callNumber"][0])
							del all_data_combine["callNumber"][0:3]
						else:
							reply = make_send_value(0)
						self.conn.send(reply)
						print("To client--------- : ",reply)
						
					elif data.decode() == 'quit':
						self.conn.send('Terminate'.encode())
						self.conn.close()
						self.s.close()
						break

					else:
						reply = 'Unknown command'
						self.conn.send(reply.encode())
						print("To client--------- : ", reply)

				except Exception as e:
					print(e)
					self.conn.close()
					self.s.close()
					break
#----------------------------------------------------------------------

def tracking(cp):
	global all_data_combine,send_value

	for i in range(2,9):
		for j in range(1,4):
			all_data_combine["callNumber"].append(i*20)

	for i in range(9,1,-1):
		for j in range(1,4):
			all_data_combine["callNumber"].append(i*20)

	all_data_combine["personNumber"] = int(len(all_data_combine["callNumber"])/3)

	print(all_data_combine)

	while True:
		input("press Enter\n") # avoid to infinite loop, remove this.
		for i in range(3):
			all_data_combine["callNumber"].append(11)

		all_data_combine["personNumber"] = int(len(all_data_combine["callNumber"])/3)
		print(all_data_combine)
		cp.send_personNumber()
		


#		 ** READ **
#		 ________________________________________________________________________________________________________
#		 |																										 |
#		 |  Input here the image process code.																	 |
#		 |  You don't have to be reacted call signal, just Write the data to "all_data_combine" every moment.    |
#		 |  Data shape is "number, x, y, z". and it's in List of "callNumber" in "all_data_combine" dictionary   |
#		 |  So if you want to input the data, you can access global variable.									 |
#		 |  Then, Comunity Thread process rest of stuff.														 |
#		 |																									     |
#		 |  I suggest a way to input the data to "all_data_combine", you should use "list.append("somthing")"	 |
#		 |  --> all_data_combine["callNumber"].append("something")												 |
#		 |																										 |
#		 |_______________________________________________________________________________________________________|
#           ||
#    (\__/) ||
#    (•ㅅ•) ||
#    / 　 づ



if __name__ == '__main__':
	cp = comunicateProgram()
	thread = threading.Thread(target= cp.socket_comunity_thread, args=())
	thread.daemon = True # when main code is shut. deamon thread is shut too.
	thread.start()
	tracking(cp)