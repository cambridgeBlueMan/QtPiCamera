"""
derived from desginer file and used in development of composite sliders
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.contrast = CompositeDial(self.centralwidget)
        self.contrast.setGeometry(QtCore.QRect(60, 110, 131, 60))
        self.contrast.setProperty("maximum", 30)
        self.contrast.setProperty("minimum", -30)
        self.contrast.setProperty("value", 0)
        self.contrast.setObjectName("contrast")
        self.twattock = CompositeDial(self.centralwidget)
        self.twattock.setGeometry(QtCore.QRect(40, 220, 131, 60))
        self.twattock.setProperty("maximum", 30)
        self.twattock.setProperty("minimum", -30)
        self.twattock.setProperty("value", 0)
        self.twattock.setObjectName("twattock")
        self.widget = CompositeSlider(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 430, 371, 80))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.contrast.setProperty("cameraOption", _translate("MainWindow", "brightness"))
        self.twattock.setProperty("cameraOption", _translate("MainWindow", "brightness"))

from mysliders import CompositeDial, CompositeSlider
