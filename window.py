# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 305)
        MainWindow.setStyleSheet("background:#3d3d3d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_status_sub_message = QtWidgets.QLabel(self.centralwidget)
        self.label_status_sub_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_sub_message.setObjectName("label_status_sub_message")
        self.gridLayout_2.addWidget(self.label_status_sub_message, 4, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_start_end = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_end.setStyleSheet("QPushButton{\n"
"    background-color: #fff; /* Green */\n"
"    border: none;\n"
"    color: #000;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 20px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#f1f2f6;\n"
"}\n"
"")
        self.pushButton_start_end.setObjectName("pushButton_start_end")
        self.gridLayout.addWidget(self.pushButton_start_end, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 1, 1, 1)
        self.label_status_message = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_status_message.setFont(font)
        self.label_status_message.setStyleSheet("color:rgb(255, 80, 57);")
        self.label_status_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_message.setObjectName("label_status_message")
        self.gridLayout_2.addWidget(self.label_status_message, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_start_end.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_status_sub_message.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">your internet is </span><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">not private</span></p></body></html>"))
        self.pushButton_start_end.setText(_translate("MainWindow", "Start"))
        self.label_status_message.setText(_translate("MainWindow", "DISCONNECTED"))
