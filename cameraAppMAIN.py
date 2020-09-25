from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from picamera import PiCamera

from io import BytesIO
from time import sleep
# used to test if file exists
import os.path
import datetime
from os import path
import json
#camera = PiCamera() 
"""
MainWindow.ui is a file initially created in QtDesigner.  This file is then translated into
a single Python class called Ui_MainWindow by pyuic5.

(substitue MainWindow for the name you gave the Dialo or MianWindow object in Designer)
"""

    
from cameraApp import *
#from settings import camvals
#print(camvals)
"""
The Code_MainWindow class is to define all the logic and functions for the program to operate
Most of these functions will already have been referenced in the designer file via signal/slot connections

Note that this class has to inherit from the relevant parent class. In this case a QDialog,
but could as easily be a QMainMenu

remember that this means that this is a Dialog window or other window with some added code/methods

This Dialog window with added code will be passed to an instance of the automatically
created Designer class. This designer created class has methods to draw the various widgets and associate them 
with the passed instance of the code/widget class
"""
class Code_MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        with open("settings.json", "r") as settings:
            self.camvals = json.load(settings)
            print(self.camvals)
 
    #Add the additional methods/ data structures etc here
    def setZoomStart(*args):
        zoomStartVals =  (ui.zStartX.value(), ui.zStartY.value(), ui.zStartHeight.value(), ui.zStartWidth.value())
        print (zoomStartVals)
 
    def setZoomEnd(*args):
        zoomEndVals =  (ui.zEndX.value(), ui.zEndY.value(), ui.zEndHeight.value(), ui.zEndWidth.value())
        print (zoomEndVals)
    
    def snapAndSave(*args):  
        filename = args[0].camvals["stillFileRoot"] + '{:04d}'.format(args[0].camvals["fileCounter"]) + '.' + args[0].camvals["stillFormat"]
        # does the file exist? if not then write it
        if path.exists(filename):
            # if file exists then put the picture to a stream object
            #stream = args[0].imgToStream()
            stream = BytesIO()
            camera.capture(stream, 'jpeg')
            # now find out what to do with it
            msgBox = QMessageBox()
            msgBox.setWindowTitle("FileExists")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("This file exists, do you want to overwrite it?")
            msgBox.setStandardButtons(QMessageBox.Save|QMessageBox.Cancel)
            appendButton = QPushButton( "append timestamp")
            msgBox.addButton(appendButton, QMessageBox.YesRole)
            msgBox.setDefaultButton(appendButton)
            
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                # if save then overwite existing file
                with open (filename, 'wb') as f:
                    #print(stream)
                    f.write(stream.getbuffer())
                    args[0].showImage(filename)
            if ret == QMessageBox.Cancel:
                # if cancel then get rid of the buffer
                stream.close()
                pass
            if ret == 0: #appendButton:
                # if save with an appended timestamp then save the buffer/stream with the timestamp
                filename = args[0].camvals["stillFileRoot"] + '{:04d}'.format(args[0].camvals["fileCounter"]) + str(datetime.datetime.now()) + '.'+ args[0].camvals["stillFormat"]
                with open (filename, 'wb') as f:
                    f.write(stream.getbuffer())
                    args[0].showImage(filename)
        else:
            # take a picture and increment the counter
            camera.capture(filename)
            args[0].incFileCounter()
            args[0].showImage(filename)
    
    def showImage(*args):
        pixmap = QtGui.QPixmap(args[1])
        pixmapResized = pixmap.scaled(800, 600, QtCore.Qt.KeepAspectRatio)
        ui.imgContainer.setPixmap(pixmapResized) #.scaled(size,Qt.keepAspectRatio))
    def incFileCounter(*args):
        # increments the file counter and saves it to the settings file
        print(args)
        args[0].camvals["fileCounter"] = args[0].camvals["fileCounter"] + 1
        with open("settings.json", "w") as settings:
            json.dump(args[0].camvals, settings, indent = 4)
            
    def imgToStream(*args):
        # gets a picture and puts it intoo a stream/buffer object
        stream = BytesIO()
        camera.capture(stream, 'jpeg')
        return stream.getbuffer()
    
    def snapAndHold(*args):
        print("in snap and hold")
        stream = self.imgToStream()
        # save for this scenario
        with open ("aPic.jpg", 'wb') as f:
            f.write(stream.getbuffer())
        # function here to put snap data to a BytesIO() object and then prompt for a save
        
    def setFileRoot(*args):
        pass
    def isDateStamp(*args):
        pass
    def isCounter(*args):
        pass
    def showPreview(*args):
        if args[1] == True:
            x = int(camera.resolution[0]/2)
            y = int(camera.resolution[1]/2)
            camera.start_preview(fullscreen=False, window = (0, 0,x,y))
        else:
            camera.stop_preview()
    def setPreviewSize(*args):
        pass 
    
class MyCamera(PiCamera):
    def __init__(self):
        super().__init__()
        self.setupCamera()
        #filename = "/home/pi/Pictures/file1.jpg" 
    def setupCamera(self):
        # retrieve various stuff from a ini file
        #self.filename = filename
        with open("settings.json", "r") as settings:
            self.camvals = json.load(settings)
        self.vidres = self.camvals["vidres"]
        self.imgres = self.camvals["imgres"]
        self.resolution = tuple(self.imgres)
        print(self.resolution)
        #pass   
        
if __name__ == "__main__":
    import sys
   
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_MainWindow()
    # instantiate an object from the imported Ui_MainWindow class
    ui = Ui_MainWindow()
    # pass a reference to the MainWindow object to the setupUi method of the Ui_MainWindow instance ui
    ui.setupUi(MainWindow)
     # instantiate a camera
    camera = MyCamera()
    # show it!
    MainWindow.show()
    sys.exit(app.exec_())


 