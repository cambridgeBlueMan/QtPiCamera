# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class myWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("myWidget")
        self.resize(281, 107)
        self.dial_2 = QtWidgets.QDial(self)
        self.dial_2.setGeometry(QtCore.QRect(50, 30, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 50, 50, 32))
        self.spinBox_2.setObjectName("spinBox_2")


        self.dial_2.sliderMoved['int'].connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged['int'].connect(self.dial_2.setValue)
        self.dial_2.sliderMoved['int'].connect(self.doWork)
        self.spinBox_2.valueChanged['int'].connect(self.doWork)
        QtCore.QMetaObject.connectSlotsByName(self)

    def doWork(self):
        print ("in do work")
