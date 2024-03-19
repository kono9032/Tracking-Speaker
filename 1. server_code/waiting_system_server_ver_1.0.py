#blid error -> netstat -an -o, taskkill /f /pid 1234

import cv2
import numpy as np
import sys, os
import socket
import time
import threading
from struct import *

import copy

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

HOST = '172.30.1.14'
#HOST = '192.168.0.4'
PORT = 12345


all_data_combine = {"personNumber":0, "callNumber":[], "coordinate":[]}
#{personNumber:0 , callNumber:[123,124...], coordinate:[x,y,x,y,]}

call_number = 0
count_flag = False
tracking_start_flag = False
tracking_stop_flag = False
(soc, conn, addr) = None, None, None


# create new socket -----------------------------------------------
def MakeSocket():
	global soc, conn, addr
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("socket created")
	soc.settimeout(None)
	soc.bind((HOST,PORT))
	soc.listen()
	print ('Socket awaiting messages')
	(conn, addr) = soc.accept()
	print ('Connected :', conn,addr)


def make_send_value(callNumber):
	val = []
	if (not(callNumber)): #if no callNumber, just send personNumber.
		val.append(all_data_combine["personNumber"])
		send_value = pack('H', val[0])

	else: #send all requested data.
		val.append(all_data_combine["personNumber"])
		val.append(all_data_combine["callNumber"][0])
		for i in range (2):
			val.append(all_data_combine["coordinate"][i])
		send_value = pack('HHHH', val[0], val[1], val[2], val[3])
	return send_value

def send_personNumber(self):
		reply = make_send_value(0)
		if(conn): conn.send(reply)

class comunicateProgram():
	def __init__(self, parent=None):
		self.socket_comunity_thread()

	def socket_comunity_thread(self):
		global all_data_combine, call_number, tracking_start_flag, tracking_stop_flag
		# comunicate with client --------------------------------------
		while True:
			try:
				data = conn.recv(1024).decode()
				print ('From client------- : ' + data)
				reply = ''
				if data == 'connected':
					reply = make_send_value(0)
					conn.send(reply)
					print("To client--------- : ",reply)

				elif data == 'call':
					if(all_data_combine["personNumber"] != 0):
						tracking_stop_flag = True
						while(tracking_stop_flag): pass

					if(all_data_combine["personNumber"] != 0):
						if (all_data_combine["callNumber"]):
							all_data_combine["personNumber"] -= 1
							reply = make_send_value(all_data_combine["callNumber"][0])
							del all_data_combine["callNumber"][0]
							del all_data_combine["coordinate"][0:2]
						else:
							reply = make_send_value(0)
					else:
						reply = make_send_value(0)
					conn.send(reply)
					print("To client--------- : ",reply)
					
				elif data == 'quit':
					conn.send('Terminate'.encode())
					conn.close()
					soc.close()
					break

				elif data.isdigit():
					call_number = int(data)
					all_data_combine["callNumber"].append(call_number)
					all_data_combine["personNumber"] += 1
					reply = make_send_value(0)

					tracking_start_flag = True
					conn.send(reply)
					print("To client--------- : ", reply)

				else:
					reply = 'Unknown command'
					conn.send(reply.encode())
					print("To client--------- : ", reply)
			
			except KeyboardInterrupt:
				conn.close()
				soc.close()
				sys.exit()

			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(e, exc_type, fname, exc_tb.tb_lineno)
				conn.close()
				soc.close()
				break
		
		MakeSocket()
		self.socket_comunity_thread()
#----------------------------------------------------------------------
def visionTracking():
	global tracking_start_flag, all_data_combine, tracking_stop_flag
	trackerName = 'tld'

	OPENCV_OBJECT_TRACKERS = {
	    "csrt": cv2.TrackerCSRT_create,
	    "kcf": cv2.TrackerKCF_create,
	    "boosting": cv2.TrackerBoosting_create,
	    "mil": cv2.TrackerMIL_create,
	    "tld": cv2.TrackerTLD_create,
	    "medianflow": cv2.TrackerMedianFlow_create,
	    "mosse": cv2.TrackerMOSSE_create
	}

	trackers = cv2.MultiTracker_create()
	cap = cv2.VideoCapture(0)

	while (True):
	    ret, img = cap.read()
	    # print('face:',type(faces))

	    (success, boxes) = trackers.update(img)

	    for boxs in boxes:
	        (x2, y2, w2, h2) = [int(v) for v in boxs]
	        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
	        point = (x2, y2, w2, h2)

	    def track(facez):
	        box = tuple(facez)
	        tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
	        trackers.add(tracker, img, box)

	    def lopoint(boxes1):
	        dela = boxes1.tolist()
	        del dela[0]
	        for i in dela:
	            save = []
	            for ii in i:
	                save.append(ii)
	            box = tuple(save)
	            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
	            trackers.add(tracker, img, box)
	            save.clear()

	    cv2.imshow('frame', img)

	    if tracking_start_flag == True:
	        sendlo = [320-50,240-50,100,100]
	        track(sendlo)
	        tracking_start_flag = False
	    
	    if tracking_stop_flag == True:
	        lo_x = float(boxes[0][0])+(float(boxes[0][2])/2)
	        lo_y = float(boxes[0][1])+(float(boxes[0][3])/2)
	        print('Mid[x]:',lo_x,'     Mid[y]:',lo_y)
	        trackers.clear()
	        trackers = cv2.MultiTracker_create()
	        lopoint(boxes)

	        all_data_combine["coordinate"].append(int(lo_x/3.555))
	        all_data_combine["coordinate"].append(int(lo_y/2.666))
	        tracking_stop_flag = False

	    cv2.waitKey(1)

if __name__ == '__main__':
	thread = threading.Thread(target= visionTracking, args=())
	thread.daemon = True # when main code is shut. deamon thread is shut too.
	thread.start()
	MakeSocket()
	cp = comunicateProgram()
	