# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.call_button = QtWidgets.QPushButton(self.centralwidget)
        self.call_button.setGeometry(QtCore.QRect(410, 115, 171, 284))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.call_button.setFont(font)
        self.call_button.setStyleSheet("border:none;")
        self.call_button.setText("")
        self.call_button.setObjectName("call_button")
        self.person_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.person_lcdNumber.setGeometry(QtCore.QRect(70, 130, 301, 131))
        self.person_lcdNumber.setStyleSheet("border:none;")
        self.person_lcdNumber.setObjectName("person_lcdNumber")
        self.call_number_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.call_number_lcdNumber.setGeometry(QtCore.QRect(70, 270, 301, 121))
        self.call_number_lcdNumber.setStyleSheet("border:none;")
        self.call_number_lcdNumber.setDigitCount(5)
        self.call_number_lcdNumber.setProperty("value", 0.0)
        self.call_number_lcdNumber.setProperty("intValue", 0)
        self.call_number_lcdNumber.setObjectName("call_number_lcdNumber")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(0, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(57, 130, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(57, 280, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.recall_button = QtWidgets.QPushButton(self.centralwidget)
        self.recall_button.setGeometry(QtCore.QRect(587, 115, 160, 285))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.recall_button.setFont(font)
        self.recall_button.setStyleSheet("border:none;")
        self.recall_button.setText("")
        self.recall_button.setObjectName("recall_button")
        self.quit_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.quit_pushbutton.setGeometry(QtCore.QRect(130, 440, 51, 31))
        self.quit_pushbutton.setStyleSheet("border:none;")
        self.quit_pushbutton.setText("")
        self.quit_pushbutton.setObjectName("quit_pushbutton")
        self.connect_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pushButton.setGeometry(QtCore.QRect(58, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.connect_pushButton.setFont(font)
        self.connect_pushButton.setStyleSheet("border: none;")
        self.connect_pushButton.setObjectName("connect_pushButton")
        self.host_ip_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.host_ip_spinBox.setGeometry(QtCore.QRect(700, 60, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.host_ip_spinBox.setFont(font)
        self.host_ip_spinBox.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.host_ip_spinBox.setFrame(False)
        self.host_ip_spinBox.setProperty("value", 5)
        self.host_ip_spinBox.setObjectName("host_ip_spinBox")
        self.host_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.host_ip_label.setGeometry(QtCore.QRect(570, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.host_ip_label.setFont(font)
        self.host_ip_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.host_ip_label.setObjectName("host_ip_label")
        self.socket_status_label = QtWidgets.QLabel(self.centralwidget)
        self.socket_status_label.setGeometry(QtCore.QRect(430, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.socket_status_label.setFont(font)
        self.socket_status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.socket_status_label.setStyleSheet("border : none;")
        self.socket_status_label.setText("")
        self.socket_status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.socket_status_label.setObjectName("socket_status_label")
        self.time_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.time_label_2.setGeometry(QtCore.QRect(640, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_label_2.setFont(font)
        self.time_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label_2.setObjectName("time_label_2")
        self.host_ip_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.host_ip_label_2.setGeometry(QtCore.QRect(600, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.host_ip_label_2.setFont(font)
        self.host_ip_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.host_ip_label_2.setObjectName("host_ip_label_2")
        self.disconnect_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_pushButton.setGeometry(QtCore.QRect(150, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.disconnect_pushButton.setFont(font)
        self.disconnect_pushButton.setStyleSheet("border: none;")
        self.disconnect_pushButton.setObjectName("disconnect_pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.graphicsView.setStyleSheet("background-image: url(:/img/background4.PNG);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.call_button.raise_()
        self.person_lcdNumber.raise_()
        self.call_number_lcdNumber.raise_()
        self.time_label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.recall_button.raise_()
        self.quit_pushbutton.raise_()
        self.connect_pushButton.raise_()
        self.host_ip_spinBox.raise_()
        self.host_ip_label.raise_()
        self.socket_status_label.raise_()
        self.time_label_2.raise_()
        self.host_ip_label_2.raise_()
        self.disconnect_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_label.setText(_translate("MainWindow", "2021-10-23 토"))
        self.label_3.setText(_translate("MainWindow", "대기 인원 수"))
        self.label_4.setText(_translate("MainWindow", "호출 대상 번호"))
        self.connect_pushButton.setText(_translate("MainWindow", "Connect"))
        self.host_ip_label.setText(_translate("MainWindow", "HOST : "))
        self.time_label_2.setText(_translate("MainWindow", "2021.08.04. 12:22"))
        self.host_ip_label_2.setText(_translate("MainWindow", "192.168.0."))
        self.disconnect_pushButton.setText(_translate("MainWindow", "Disconnect"))
import client_GUI_img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
