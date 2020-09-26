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
from cameraApp import *
#from settings import camvals
#print(camvals)

class Code_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # instantiate a camera
        self.camera = MyCamera()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        with open("settings.json", "r") as settings:
            self.camvals = json.load(settings)
            print(self.camvals)
 
    #Add the additional methods/ data structures etc here
    def setZoomStart(self):
        zoomStartVals =  (self.ui.zStartX.value(), self.ui.zStartY.value(), self.ui.zStartHeight.value(), self.ui.zStartWidth.value())
        print (zoomStartVals)
 
    def setZoomEnd(self):
        zoomEndVals =  (self.ui.zEndX.value(), self.ui.zEndY.value(), self.ui.zEndHeight.value(), self.ui.zEndWidth.value())
        print (zoomEndVals)
    
    def snapAndSave(self):  
        filename = self.camvals["stillFileRoot"] + '{:04d}'.format(self.camvals["fileCounter"]) + '.' + self.camvals["stillFormat"]
        # does the file exist? if not then write it
        if path.exists(filename):
            # if file exists then put the picture to a stream object
            #stream = self.imgToStream()
            stream = BytesIO()
            self.camera.capture(stream, 'jpeg')
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
                    self.showImage(filename)
            if ret == QMessageBox.Cancel:
                # if cancel then get rid of the buffer
                stream.close()
                pass
            if ret == 0: #appendButton:
                # if save with an appended timestamp then save the buffer/stream with the timestamp
                filename = self.camvals["stillFileRoot"] + '{:04d}'.format(self.camvals["fileCounter"]) + str(datetime.datetime.now()) + '.'+ self.camvals["stillFormat"]
                with open (filename, 'wb') as f:
                    f.write(stream.getbuffer())
                    self.showImage(filename)
        else:
            # take a picture and increment the counter
            self.camera.capture(filename)
            self.incFileCounter()
            self.showImage(filename)
    
    def showImage(self, filename):
        pixmap = QtGui.QPixmap(filename)
        pixmapResized = pixmap.scaled(800, 600, QtCore.Qt.KeepAspectRatio)
        self.ui.imgContainer.setPixmap(pixmapResized) #.scaled(size,Qt.keepAspectRatio))
    def incFileCounter(self):
        # increments the file counter and saves it to the settings file
        print(self)
        self.camvals["fileCounter"] = self.camvals["fileCounter"] + 1
        with open("settings.json", "w") as settings:
            json.dump(self.camvals, settings, indent = 4)
            
    def imgToStream(self):
        # gets a picture and puts it intoo a stream/buffer object
        stream = BytesIO()
        self.camera.capture(stream, 'jpeg')
        return stream.getbuffer()
    
    def snapAndHold(self):
        print("in snap and hold")
        stream = self.imgToStream()
        # save for this scenario
        with open ("aPic.jpg", 'wb') as f:
            f.write(stream)
        
    def setFileRoot(*args):
        pass
    def isDateStamp(*args):
        pass
    def isCounter(*args):
        pass
    def showPreview(self, state):
        if state == True:
            x = int(self.camera.resolution[0]/2)
            y = int(self.camera.resolution[1]/2) 
            self.camera.start_preview(fullscreen=False, window = (0, 0,x,y))
        else:
            self.camera.stop_preview()
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
    sys.exit(app.exec_())


 