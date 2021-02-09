# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraApp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 850)
        MainWindow.setIconSize(QtCore.QSize(128, 96))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(670, 680, 801, 111))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 99, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 20, 99, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.isCounter = QtWidgets.QRadioButton(self.tab)
        self.isCounter.setGeometry(QtCore.QRect(620, 20, 119, 27))
        self.isCounter.setChecked(True)
        self.isCounter.setObjectName("isCounter")
        self.isDatestamp = QtWidgets.QRadioButton(self.tab)
        self.isDatestamp.setGeometry(QtCore.QRect(500, 20, 119, 27))
        self.isDatestamp.setObjectName("isDatestamp")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(270, 20, 160, 34))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.fileRoot = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.fileRoot.setObjectName("fileRoot")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fileRoot)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.vidPosSlider = QtWidgets.QSlider(self.tab_2)
        self.vidPosSlider.setGeometry(QtCore.QRect(220, 30, 571, 26))
        self.vidPosSlider.setMaximum(1000)
        self.vidPosSlider.setOrientation(QtCore.Qt.Horizontal)
        self.vidPosSlider.setObjectName("vidPosSlider")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 196, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startRecordVid = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startRecordVid.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/media-record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startRecordVid.setIcon(icon)
        self.startRecordVid.setObjectName("startRecordVid")
        self.horizontalLayout_2.addWidget(self.startRecordVid)
        self.playVid = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playVid.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playVid.setIcon(icon1)
        self.playVid.setObjectName("playVid")
        self.horizontalLayout_2.addWidget(self.playVid)
        self.stopVid = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopVid.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/media-playback-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopVid.setIcon(icon2)
        self.stopVid.setObjectName("stopVid")
        self.horizontalLayout_2.addWidget(self.stopVid)
        self.pauseVid = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pauseVid.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/media-playback-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseVid.setIcon(icon3)
        self.pauseVid.setObjectName("pauseVid")
        self.horizontalLayout_2.addWidget(self.pauseVid)
        self.tabWidget.addTab(self.tab_2, "")
        self.previewVisible = QtWidgets.QCheckBox(self.centralwidget)
        self.previewVisible.setGeometry(QtCore.QRect(670, 650, 101, 27))
        self.previewVisible.setObjectName("previewVisible")
        self.resizePreview = QtWidgets.QSlider(self.centralwidget)
        self.resizePreview.setGeometry(QtCore.QRect(790, 650, 591, 26))
        self.resizePreview.setOrientation(QtCore.Qt.Horizontal)
        self.resizePreview.setObjectName("resizePreview")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 321, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lstartX = QtWidgets.QLabel(self.formLayoutWidget)
        self.lstartX.setObjectName("lstartX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lstartX)
        self.lstartY = QtWidgets.QLabel(self.formLayoutWidget)
        self.lstartY.setObjectName("lstartY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lstartY)
        self.zStartY = QtWidgets.QSlider(self.formLayoutWidget)
        self.zStartY.setMinimum(1)
        self.zStartY.setMaximum(3040)
        self.zStartY.setOrientation(QtCore.Qt.Horizontal)
        self.zStartY.setObjectName("zStartY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.zStartY)
        self.wStartWidth = QtWidgets.QLabel(self.formLayoutWidget)
        self.wStartWidth.setObjectName("wStartWidth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wStartWidth)
        self.zStartWidth = QtWidgets.QSlider(self.formLayoutWidget)
        self.zStartWidth.setMinimum(1)
        self.zStartWidth.setMaximum(4056)
        self.zStartWidth.setSliderPosition(2028)
        self.zStartWidth.setOrientation(QtCore.Qt.Horizontal)
        self.zStartWidth.setObjectName("zStartWidth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zStartWidth)
        self.lStartHeight = QtWidgets.QLabel(self.formLayoutWidget)
        self.lStartHeight.setObjectName("lStartHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lStartHeight)
        self.zStartHeight = QtWidgets.QSlider(self.formLayoutWidget)
        self.zStartHeight.setMinimum(1)
        self.zStartHeight.setMaximum(3040)
        self.zStartHeight.setSliderPosition(1520)
        self.zStartHeight.setOrientation(QtCore.Qt.Horizontal)
        self.zStartHeight.setObjectName("zStartHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.zStartHeight)
        self.fixStartZoom = QtWidgets.QPushButton(self.formLayoutWidget)
        self.fixStartZoom.setObjectName("fixStartZoom")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fixStartZoom)
        self.zStartX = QtWidgets.QSlider(self.formLayoutWidget)
        self.zStartX.setMinimum(1)
        self.zStartX.setMaximum(4056)
        self.zStartX.setOrientation(QtCore.Qt.Horizontal)
        self.zStartX.setObjectName("zStartX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zStartX)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 270, 321, 191))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lEndX = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lEndX.setObjectName("lEndX")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lEndX)
        self.lEndY = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lEndY.setObjectName("lEndY")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lEndY)
        self.zEndY = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.zEndY.setMinimum(1)
        self.zEndY.setMaximum(3040)
        self.zEndY.setSliderPosition(1)
        self.zEndY.setOrientation(QtCore.Qt.Horizontal)
        self.zEndY.setObjectName("zEndY")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.zEndY)
        self.lEndWidth = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lEndWidth.setObjectName("lEndWidth")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lEndWidth)
        self.zEndWidth = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.zEndWidth.setMinimum(1)
        self.zEndWidth.setMaximum(4056)
        self.zEndWidth.setSliderPosition(4056)
        self.zEndWidth.setOrientation(QtCore.Qt.Horizontal)
        self.zEndWidth.setObjectName("zEndWidth")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zEndWidth)
        self.lEndHeight = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lEndHeight.setObjectName("lEndHeight")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lEndHeight)
        self.zEndHeight = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.zEndHeight.setMinimum(1)
        self.zEndHeight.setMaximum(3040)
        self.zEndHeight.setSliderPosition(3040)
        self.zEndHeight.setOrientation(QtCore.Qt.Horizontal)
        self.zEndHeight.setObjectName("zEndHeight")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.zEndHeight)
        self.fixEndZoom = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.fixEndZoom.setObjectName("fixEndZoom")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fixEndZoom)
        self.zEndX = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.zEndX.setMinimum(1)
        self.zEndX.setMaximum(4056)
        self.zEndX.setSliderPosition(1)
        self.zEndX.setOrientation(QtCore.Qt.Horizontal)
        self.zEndX.setObjectName("zEndX")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zEndX)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 91, 22))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(40, 240, 81, 22))
        self.label_14.setObjectName("label_14")
        self.imgContainer = QtWidgets.QLabel(self.centralwidget)
        self.imgContainer.setGeometry(QtCore.QRect(670, 40, 800, 600))
        self.imgContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.imgContainer.setText("")
        self.imgContainer.setObjectName("imgContainer")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 530, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 590, 118, 24))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.thumbnails = QtWidgets.QListWidget(self.centralwidget)
        self.thumbnails.setGeometry(QtCore.QRect(500, 40, 140, 601))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.thumbnails.setFont(font)
        self.thumbnails.setIconSize(QtCore.QSize(128, 96))
        self.thumbnails.setViewMode(QtWidgets.QListView.IconMode)
        self.thumbnails.setWordWrap(True)
        self.thumbnails.setObjectName("thumbnails")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.fixStartZoom.clicked.connect(MainWindow.setZoomStart)
        self.fixEndZoom.clicked.connect(MainWindow.setZoomEnd)
        self.pushButton_4.clicked.connect(MainWindow.snapAndSave)
        self.pushButton_5.clicked.connect(MainWindow.snapAndHold)
        self.fileRoot.textChanged['QString'].connect(MainWindow.setFileRoot)
        self.isDatestamp.clicked.connect(MainWindow.isDateStamp)
        self.isCounter.clicked.connect(MainWindow.isCounter)
        self.previewVisible.clicked['bool'].connect(MainWindow.showPreview)
        self.resizePreview.valueChanged['int'].connect(MainWindow.setPreviewSize)
        self.tabWidget.currentChanged['int'].connect(MainWindow.setupVid)
        self.startRecordVid.clicked['bool'].connect(MainWindow.doRecordVid)
        self.playVid.clicked['bool'].connect(MainWindow.doPlayVid)
        self.stopVid.clicked.connect(MainWindow.doStopVid)
        self.pauseVid.clicked['bool'].connect(MainWindow.doPauseVid)
        self.vidPosSlider.sliderMoved['int'].connect(MainWindow.setPosition)
        self.thumbnails.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.doThumbnailClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Snap/Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Snap/Hold"))
        self.isCounter.setText(_translate("MainWindow", "Counter "))
        self.isDatestamp.setText(_translate("MainWindow", "Datestamp"))
        self.label_15.setText(_translate("MainWindow", "File root"))
        self.fileRoot.setText(_translate("MainWindow", "img_"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Still"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Video"))
        self.previewVisible.setText(_translate("MainWindow", "Preview"))
        self.lstartX.setText(_translate("MainWindow", "X"))
        self.lstartY.setText(_translate("MainWindow", "Y"))
        self.wStartWidth.setText(_translate("MainWindow", "Width"))
        self.lStartHeight.setText(_translate("MainWindow", "Height"))
        self.fixStartZoom.setText(_translate("MainWindow", "Apply"))
        self.lEndX.setText(_translate("MainWindow", "X"))
        self.lEndY.setText(_translate("MainWindow", "Y"))
        self.lEndWidth.setText(_translate("MainWindow", "Width"))
        self.lEndHeight.setText(_translate("MainWindow", "Height"))
        self.fixEndZoom.setText(_translate("MainWindow", "Apply"))
        self.label_13.setText(_translate("MainWindow", "Zoom Start"))
        self.label_14.setText(_translate("MainWindow", "Zoom End"))

import resource_rc
