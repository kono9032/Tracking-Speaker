from __future__ import print_function
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import pyqtSignal
from struct import pack, unpack, calcsize
from main_GUI_ui import*
from TTS_play import*
from time import sleep
from bluetooth import*

import serial  
import time
import socket
import threading

#HOST = '192.168.0.4'
HOST = '192.168.8.101'
PORT = 12345

socket_flag = False
send_flag = False
socket_status = ''
send_value = ''


person_count = 0
call_number = 0
available_value = []

y = ""
newcode = ""

ser = serial.Serial(                 
        port='/dev/ttyAMA1',         
        baudrate=115200,               
        parity=serial.PARITY_NONE,      
        stopbits=serial.STOPBITS_ONE,   
        bytesize=serial.EIGHTBITS,        
        timeout=0.2                      
        )

def SerialRead(self):
    global send_value, socket_flag
    while 1:
        if(ser.inWaiting() > 0):
            msg = ser.readline().decode()
            print("From Client:",msg)
            send_value = msg
            socket_flag = True

def SerialWrite(msg):
	ser.write(str(msg).encode('utf-8'))


def make_receive_value(reply):
	received_value = []
	available_value = []
	if(len(reply)>2):
		for i in range(4):
			received_value.append(reply[i*2:i*2+2]) 
		for i in range(4):
			available_value.append(unpack("H", received_value[i])[0])#'H'unsigned short 2byte
	else:
		received_value.append(reply[0:2])
		print(received_value)
		available_value.append(unpack("H", received_value[0])[0])#'H'unsigned short 2byte
	print(received_value, "<---->", available_value)
	return available_value

def socket_thread(self,ui):
	global HOST, socket_status, socket_flag, send_value, person_count, call_number,available_value
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	#try to connect socket --------------------------------------
	try:
		s.connect((HOST,PORT))
	except Exception as e:
		socket_status = "Connect Fail, retry other HOST IP"
		ui.uiUpdateDelegate.emit(1)
		print("connecting Fail")
		return 0
	
	send_value = ''
	socket_status = "connected!!"
	print('connected')
	call_number = 0
	ui.uiUpdate_for_connect.emit(1)

	send_value = 'connected'
	socket_flag = True

	#comunicate with server -------------------------------------
	while True:
		if socket_flag:
			s.send(send_value.encode())
			print("To   server:",send_value)
			reply = s.recv(1024)
			# if it's the command
			if reply == b'Terminate':
				socket_status = "Discunnected."
				print('discunnected')
				socket_flag = False
				break

			elif reply == b'Unknown command':
				print('Something Wrong...')
				socket_flag = False

			elif reply == b'thank you':
				socket_flag = False

			# if it's not command, save the received value
			else:
				available_value = make_receive_value(reply)

			# renew the display number
			person_count = available_value[0]
			if(len(available_value)>1):
				call_number = available_value[1]
			ui.uiUpdate_for_connect.emit(1)
			socket_flag = False
			SerialWrite(person_count)
			print("to   Client:",person_count)
			#update person count everymoment.
		else:
			try:
				reply = s.recv(1024)
				person_count = make_receive_value(reply)[0]
				ui.uiUpdate_for_connect.emit(1)
				SerialWrite(person_count)
			except:
				pass

def comunicate_speaker():
	global available_value, send_flag
	client_socket=BluetoothSocket( RFCOMM )
	state = client_socket.connect_ex(("98:D3:11:FC:3F:8E",1)) #98:D3:11:FC:3F:8E, 98:d3:91:fd:c4:27 
	while True:
		if state:
			client_socket=BluetoothSocket( RFCOMM )
			state = client_socket.connect_ex(("98:D3:11:FC:3F:8E",1))
			print("waiting...")
			QtTest.QTest.qWait(1500)
		else:
			try:
				if send_flag == True:
					while(socket_flag):pass
					
					if(available_value[2]>127):
						temp1 = chr(127) + chr(available_value[2]-127)
					else:
						temp1 = chr(0) + chr(available_value[2])

					if(available_value[3]>127):
						temp2 = chr(127) + chr(available_value[3]-127)
					else:
						temp2 = chr(0) + chr(available_value[3])

					value = temp1 + temp2
					print("value :%s"%value)

					client_socket.send(value)
					rev = client_socket.recv(1024)
					playSound(call_number,1)
					send_flag = False

			except ValueError as err:
					print(err)
					state = 1
					continue

# GUI structure -------------------------------------------------
class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
	global HOST 
	uiUpdateDelegate = pyqtSignal(int)
	uiUpdate_for_connect = pyqtSignal(int)

	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		initial_value = HOST[HOST.rfind('.')+1:]
		initial_value2 = HOST[:HOST.rfind('.')+1]
		self.setupUi(self)
		self.uiUpdateDelegate.connect(self.uiUpdater)
		self.uiUpdate_for_connect.connect(self.uiUpdater_connect)
		self.quit_pushbutton.clicked.connect(self.quit_pushbutton_clicked)
		self.connect_pushButton.clicked.connect(self.connect_pushButton_clicked)
		self.disconnect_pushButton.clicked.connect(self.disconnect_button_clicked)
		self.call_button.clicked.connect(self.call_button_clicked)
		self.call_button.pressed.connect(self.call_button_p)
		self.call_button.released.connect(self.call_button_r)
		self.recall_button.clicked.connect(self.recall_button_clicked)
		self.recall_button.pressed.connect(self.recall_button_p)
		self.recall_button.released.connect(self.recall_button_r)
		self.disconnect_pushButton.setDisabled(True)
		self.call_button.setDisabled(True)
		self.recall_button.setDisabled(True)
		self.host_ip_spinBox.setProperty("value", initial_value)
		self.host_ip_label_2.setText(initial_value2)
	def uiUpdater_connect(self):
		global socket_status
		self.socket_status_label.setText(socket_status) 
		self.disconnect_pushButton.setEnabled(True)
		self.call_button.setEnabled(True)
		self.recall_button.setEnabled(True)
		self.call_number_lcdNumber.setProperty("value", call_number)
		self.person_lcdNumber.setProperty("value", person_count)
		self.graphicsView.setStyleSheet("background-image: url(:/img/background.PNG);")
	def uiUpdater(self):
		global socket_status
		self.socket_status_label.setText(socket_status) 
		self.connect_pushButton.setEnabled(True)
		self.disconnect_pushButton.setDisabled(True)
		self.call_button.setDisabled(True)
		self.recall_button.setDisabled(True)
		self.graphicsView.setStyleSheet("background-image: url(:/img/background4.PNG);")

	def call_button_clicked(self):
		global socket_flag, send_value, send_flag
		if(person_count): send_flag = True
		send_value = 'call'
		socket_flag = True

	def call_button_p(self):
		self.graphicsView.setStyleSheet("background-image: url(:/img/background3.PNG);")
	def call_button_r(self):
		self.graphicsView.setStyleSheet("background-image: url(:/img/background.PNG);")


	def recall_button_clicked(self):
		thread = threading.Thread(target= playSound, args=(call_number,1))
		thread.start()

	def recall_button_p(self):
		self.graphicsView.setStyleSheet("background-image: url(:/img/background2.PNG);")
	def recall_button_r(self):
		self.graphicsView.setStyleSheet("background-image: url(:/img/background.PNG);")


	def connect_pushButton_clicked(self):
		global HOST, thread_1
		self.socket_status_label.setText("Waiting......")
		HOST = HOST[:HOST.rfind('.')+1] + str(self.host_ip_spinBox.value())

		thread_1 = threading.Thread(target= socket_thread, args=(None,ui))
		thread_1.daemon = True
		if (not(thread_1.isAlive())):
			thread_1.start()
			self.connect_pushButton.setDisabled(True)
			print('try connect')
		else:
			print('its not yet')

	def disconnect_button_clicked(self):
		global socket_flag, send_value, socket_status
		send_value = 'quit'
		socket_flag = True
		print('quit')
		socket_status = "Discunnected"
		self.call_number_lcdNumber.setProperty("value", 0)
		self.person_lcdNumber.setProperty("value", 0)
		self.uiUpdateDelegate.emit(1)

	def quit_pushbutton_clicked(self):
		global call_flag, send_value, thread_1
		send_value = 'quit'
		call_flag = True
		while 1:
			if (not(thread_1.isAlive())):
				sys.exit()

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = MyFirstGuiProgram()
	# socket communication is Executed by thread.
	thread_1 = threading.Thread(target= socket_thread, args=(None,ui))
	thread_1.daemon = True # when main code is shut. deamon thread is shut too.
	
	thread_2 = threading.Thread(target= comunicate_speaker, args=())
	thread_2.daemon = True
	thread_2.start()
	
	thread_3 = threading.Thread(target= SerialRead, args=(None,))
	thread_3.daemon = True
	thread_3.start()

	#ui.show()
	ui.showFullScreen()
	sys.exit(app.exec_())    
