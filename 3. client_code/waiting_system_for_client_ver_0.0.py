# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import pyqtSignal
from client_GUI import *
from struct import *
import serial
import threading

call_number = 110
person_number = 0
clicked_flag = False

ser = serial.Serial(               
        port='/dev/ttyS0',         
        baudrate=115200,                
        parity=serial.PARITY_NONE,       
        stopbits=serial.STOPBITS_ONE,    
        bytesize=serial.EIGHTBITS,        
        timeout=0.2                     
        )

def SerialComunication(ui):
	global clicked_flag, person_number
	while 1:
	    if(ser.inWaiting() > 0): #수신 값, 대기인원수를 받을 때 사용
	        msg = ser.readline()
	        print(msg)
	        person_number = int(msg)
	        ui.uiUpdate.emit(1)
	    elif(clicked_flag): #송신 값, 대기순번을 전송
	    	ser.write(str(call_number).encode())
	    	QtTest.QTest.qWait(500)
	    	ui.button_click_effect.emit(1)
	    	clicked_flag = False
	    	
class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
	uiUpdate = pyqtSignal(int)
	button_click_effect = pyqtSignal(int)
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		self.setupUi(self)
		self.button_click_effect.connect(self.button_effect)
		self.uiUpdate.connect(self.UiUpdate)
		self.num_button.pressed.connect(self.button_effect_p)
		self.num_button.released.connect(self.button_effect_r)
		self.quit_pushbutton.clicked.connect(self.quit_pushbutton_clicked)
		self.callNum_spinBox.setHidden(True)

	def UiUpdate(self):
		self.personNum_spinBox.setValue(person_number)

	#대기번호가 표시되고 강조하는 효과
	def button_effect(self):
		self.callNum_spinBox.setValue(call_number)
		self.callNum_spinBox.setVisible(True)
		for i in range(2):
			self.graphicsView.setStyleSheet("background-image: url(:/img/effect_1.png);")
			QtTest.QTest.qWait(500)
			self.graphicsView.setStyleSheet("background-image: url(:/img/effect_2.png);")
			QtTest.QTest.qWait(500)
		self.graphicsView.setStyleSheet("background-image: url(:/img/background.png);")
		QtTest.QTest.qWait(3000)
		self.callNum_spinBox.setHidden(True)

	#--------------------------------버튼 클릭 효과--------------------------------------
	def button_effect_p(self):
		self.graphicsView.setStyleSheet("background-image: url(:/img/background2.png);")
	def button_effect_r(self):
		global clicked_flag, call_number
		self.graphicsView.setStyleSheet("background-image: url(:/img/background.png);")
		call_number += 1
		clicked_flag = True
	#------------------------------- ---------------------------------------------------
	
	def quit_pushbutton_clicked(self):
		sys.exit()

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle('Fusion') 
	ui = MyFirstGuiProgram()	

	thread = threading.Thread(target= SerialComunication, args=(ui,))
	thread.daemon = True
	thread.start()

	#ui.show()
	ui.showFullScreen()
	sys.exit(app.exec_())