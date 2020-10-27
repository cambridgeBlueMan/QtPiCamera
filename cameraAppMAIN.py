from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from picamera import PiCamera

from io import BytesIO
from time import sleep
# used to test if file exists
import os.path
import datetime
import subprocess # allows access to command line
from os import path
import json
import vlc
import ast
#import regexp
from cameraApp import *
# my stuff
import globalfunctions as gf
#print(camVals)

class Code_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # instantiate a camera
        self.camera = MyCamera()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # now show the Ui
        self.show()
        self.camVals = gf.getSettingsFile(self.camera)
        #print(type(self.camVals))
        #print("***********************************************************************************")
        #print(self.camVals)
        self.vidres = self.camVals["vidres"]
        self.imgres = self.camVals["imgres"]
        self.resolution = tuple(self.imgres)
        # timer is used to update position slider as a video plays
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateUi)
        # is_paused indicates whether video is paused or not
        self.is_paused = False

    def updateCameraSettings(self, control, value):
        # print the control name and its value
        print(self, control, value)
        # now look for it, if you find it then set the camera and update the dictionary
        if control in self.camVals:
            print("found it!")
            # if its any zoom parm
            if control[0] == "brightness":
                print("brightness!")
                self.camVals[control] = value
            if control[0] == "saturation":
                print ("saturation!")
                self.camVals[control] = value
            if control[0] == "contrast":
                print("contrast!")
                self.camVals[control] = value
            if control[0] == "sharpness":
                print("sharpness!")
                self.camVals[control] = value
        else:
            print("not there!")
            pass
        #Add the additional methods/ data structures etc here
    def setZoomStart(self):
        zoomStartVals =  (self.camVals["zStartX"], self.camVals["zStartY"], self.camVals["zStartWidth"], self.camVals["zStartHeight"])
        print (zoomStartVals)
 
    def setZoomEnd(self):
        zoomEndVals =  (self.camVals["zEndX"], self.camVals["zEndY"], self.camVals["zEndWidth"], self.camVals["zEndHeight"])
        print (zoomEndVals)

    def setZoom(self):
        zoomVals =  (self.camVals["zoomX"], self.camVals["zoomY"], self.camVals["zoomWidth"], self.camVals["zoomHeight "])
        print (zoomVals)

    
    def snapAndSave(self):  
        filename = self.camVals["stillFileRoot"] + '{:04d}'.format(self.camVals["fileCounter"]) + '.' + self.camVals["stillFormat"]
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
                filename = self.camVals["stillFileRoot"] + '{:04d}'.format(self.camVals["fileCounter"]) \
                + str(datetime.datetime.now()).replace(':','_') + '.'+ self.camVals["stillFormat"]
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
        self.camVals["fileCounter"] = self.camVals["fileCounter"] + 1
        with open("settings.json", "w") as settings:
            json.dump(self.camVals, settings, indent = 4)
            
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
    # start of video stuff
    #
    #
    #
    #################################################################################################
    def doRecordVid(self, test):
        print ("in record vid")
        # start recording video, automatically generate file name
        # i guess this means has to have time stamp
        self.vidRoot = self.camVals["vidFileRoot"] + str(datetime.datetime.now()).replace(':','_') + '.'
        filename = self.vidRoot + self.camVals["videoFormat"]
        self.media = self.vlcObj.media_new(filename)
        self.mediaplayer.set_media(self.media)
        self.camera.start_recording(filename)
        # need to disable if recording is in progress
    def doStopVid(self, what) :
        print ("in stop vid")
        # if camera is recording then stop recording
        if self.camera.recording:
            self.camera.stop_recording() # picamera method
            # make a thumbnail?
            makeThumbnail = subprocess.run(["ffmpegthumbnailer",  "-i" ,  (self.vidRoot + self.camVals["videoFormat"]),  "-o",  (self.vidRoot + self.camVals["stillFormat"])])
            
            # following line would set icon, now set in designer, but should really be set
            # as part of the ini process and the current value stored in the json file
            #self.ui.thumbnails.setIconSize(QtCore.QSize(128, 96))
            filename = self.vidRoot + self.camVals["stillFormat"]
            self.myIcon = QtGui.QIcon(filename) 
            self.myItem = QtWidgets.QListWidgetItem(self.myIcon, filename, self.ui.thumbnails)        
            # then add it to the widget
            
        if self.mediaplayer.is_playing() == 1:
            print("media playing")
            self.mediaplayer.stop() # vlcObj.vlm_stop_media(self.vlcObj, str_to_bytes(self.media))
            #self.mediaplayer.set_position(0)
                
    def doPlayVid(self, test): 
        print (test)
        print(self.ui.imgContainer)
        self.mediaplayer.set_xwindow(int(self.ui.imgContainer.winId()))
        self.mediaplayer.set_position(0)
        print(self.mediaplayer.video_take_snapshot(0 , "filename.jpeg", 80, 60))
        self.mediaplayer.play()
        print(self.mediaplayer.video_take_snapshot(0 , "filename2.jpeg", 80, 60))        
        self.timer.start()
        # play the current video
        
    def doPauseVid(self, test):
        print ("in pause vid")
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            #self.playbutton.setText("Play")
            self.is_paused = True
            self.timer.stop()
        else:
            if self.mediaplayer.get_position() == 1:
                self.mediaplayer.stop()
            self.mediaplayer.pause()
            self.timer.start()
            self.is_paused = False
            
      
    def setPosition(self, pos):
        # called from vid pos slider
        print ("in position vid")
        print(pos)
        self.timer.stop()
        self.mediaplayer.set_position(pos / 1000.0)
        self.timer.start()
    def setupVid(self, ix):
        """
        slot called from the still/video tab selector currentChanged signal
        """
        print(self, ix)
        # if video is selected then instantiate the vlc stuff
        if ix == 1:
            self.vlcObj = vlc.Instance()
            self.media = None
            self.mediaplayer = self.vlcObj.media_player_new()
            self.is_paused = False
        else:
            # clean it all up, still to write
            pass
    def updateUi(self):
        """Updates the user interface"""

        # Set the slider's position to its corresponding media position 
        # Note that the setValue function only takes values of type int,
        # so we must first convert the corresponding media position.
        media_pos = int(self.mediaplayer.get_position() * 1000)
        print(self.mediaplayer.get_position())
        self.ui.vidPosSlider.setValue(media_pos)
        if self.mediaplayer.get_position() == 1.0:
            #self.mediaplayer.set_position(0)
            #print("hello everybody")
            self.mediaplayer.stop()
            print(self.mediaplayer.video_take_snapshot(0 , "filename.jpeg", 240, 180 ))

        # No need to call this function if nothing is played
        if not self.mediaplayer.is_playing():
            self.timer.stop()

            # After the video finished, the play button stills shows "Pause",
            # which is not the desired behavior of a media player.
            # This fixes that "bug".
            #if not self.is_paused:
            #    self.stop()

    def doThumbnailClicked(*args):
        print(args[1].text())
        
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
        # with open("settings.json", "r") as settings:
        #     self.camVals = json.load(settings)

        #self.camVals = gf.getSettingsFile(self.camera)
        #self.vidres = self.camVals["vidres"]
        #self.imgres = self.camVals["imgres"]
        #self.resolution = tuple(self.imgres)
        #print(self.resolution)
        pass
        
if __name__ == "__main__":
    import sys
   
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    mw = Code_MainWindow()
    #print(dir(mw))
    sys.exit(app.exec_())


 