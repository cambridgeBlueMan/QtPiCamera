# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testButtons.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)
"""
demoDesigner.ui is a file initially created in QtDesigner.  This file is then translated into
a single Python class called Ui_demoDesigner by pyuic5.  
"""
from QtCamera import *


"""
The Code_demoDesigner class is to define all the logic and functions for the program to operate
Most of these functions will already have been referenced in the designer file via signal/slot connections

Note that this class has to inherit from the relevant parent class. In this case a QDialog,
but could as easily be a QmainWindow

remember that this means that this is a Dialog window or other window with some added code
later an instance of this Dialog window with added code will be passed to an instance of the automatically
created Designer class. This designer created class has a method to draw the various widgets onto a passed
instance of the code/widget class
"""
class Code_mainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        self.setupMenus()
    #various code functions
    def setupMenus(self):

        # make a menu bar
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        
        # add the menus
        fileMenu = menuBar.addMenu('&File')
        viewMenu = menuBar.addMenu('&View')
        photoMenu = menuBar.addMenu('&Photo')
        videoMenu = menuBar.addMenu('V&ideo')
        helpMenu = menuBar.addMenu('&Help')
           
        # add the actions
        #file menu
        doExit = QAction('&Exit', self)
        doExit.setShortcut('Ctrl+Q')
        doExit.triggered.connect(self.close)
        fileMenu.addAction(doExit)
        doPreferences = QAction('&Preferences', self)
        doPreferences.triggered.connect(self.doPreferences)
        fileMenu.addAction(doPreferences)
        
        # view menu
        doCursors = QAction('Image c&ursors', self)
        doCursors.setShortcut('Ctrl+Shift+C')
        doCursors.triggered.connect(self.doCursors)
        viewMenu.addAction(doCursors)
        
        doAttribs = QAction('Image &attribute pane', self)
        doAttribs.setShortcut('Ctrl+Shift+A')
        doAttribs.triggered.connect(self.doAttribs)
        viewMenu.addAction(doAttribs)
        
        doPreview = QAction('&Preview pane', self)
        doPreview.setShortcut('Ctrl+Shift+P')
        doPreview.triggered.connect(self.doPreview)
        viewMenu.addAction(doPreview)
        
        doStatusBar = QAction('&Status bar', self)
        doStatusBar.triggered.connect(self.doStatusBar)
        viewMenu.addAction(doStatusBar)
        
        # photo menu
        takePicture = QAction('Take &picture', self)
        takePicture.setShortcut('Ctrl+P')
        takePicture.triggered.connect(self.takePicture)
        photoMenu.addAction(takePicture)
        
        saveImage = QAction('&Save image', self)
        saveImage.setShortcut('Ctrl+S')
        saveImage.triggered.connect(self.saveImage)
        photoMenu.addAction(saveImage)
        
        clearPicture = QAction('&Clear picture', self)
        clearPicture.setShortcut('Ctrl+C')
        clearPicture.triggered.connect(self.clearPicture)
        photoMenu.addAction(clearPicture)
        
        resetCamera = QAction('&Reset camera setup', self)
        resetCamera.setShortcut('Ctrl+R')
        resetCamera.triggered.connect(self.resetCamera)
        photoMenu.addAction(resetCamera)
        
        annotateOverlay = QAction('&Annotate/overlay', self)
        annotateOverlay.triggered.connect(self.annotateOverlay)
        photoMenu.addAction(annotateOverlay)
        
        toggleVideo = QAction('&Toggle video', self)
        toggleVideo.setShortcut('Ctrl+V')
        toggleVideo.triggered.connect(self.toggleVideo)
        videoMenu.addAction(toggleVideo)
        
    def toggleVideo(*args):
        print ('in toggle video')
        
    def annotateOverlay(*args):
        print ('in annotate/overlay')    
        
    def resetCamera(*args):
        print ('in reset camera')    
        
    def clearPicture(*args):
        print ('in clear picture')
        
    def saveImage(*args):
        print ('in save image')
        
    def takePicture(*args):
        print ('in take picture')
        
    def doPreview(*args):
        print('in Preview')
        
    def doStatusBar(*args):
        print('in do status bar')         
        
    def doAttribs(*args):
        print('in do attribs')
        
    def doCursors(*args):
        print('in do cursors')
        
    def doPreferences(*args): 
        pass
  
  # *************************************************************
  #
  # ************************************************************* 
    def setImageDenoise(*args):
        pass
    def setPortVideo(*args):
        pass
    def setPortStill(*args):
        pass
    def setVideoDenoise(*args):
        pass
    def setVideoStabilization(*args):
        pass 
        
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    mainWindow = Code_mainWindow()
    # instantiate an object from the imported Ui_demoDesigner class
    ui = Ui_MainWindow()
    # pass a reference to the demoDesigner object to the setupUi method of the Ui_demoDesigner instance ui
    ui.setupUi(mainWindow)
    # show it!
    mainWindow.show()
    sys.exit(app.exec_())


