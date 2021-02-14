from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import subprocess
import vlc
from time import sleep


def addToMediaList(self):
    """ 
    Use ffmpegthumbnailer to create a thumbnail image to represent the video
    and display the thumbnail and file name in a ListWidget

     """

    # ffmpeg -i twat.h264 -frames:v 1 -f image2 frame.png

    makeThumbnail = subprocess.Popen(["ffmpeg",  "-i" ,  (self.vidRoot + self.camvals["videoFormat"]),
    "-frames:v", "1",  "-f",  "image2",   (self.vidRoot + self.camvals["stillFormat"])])
    
    # mpeg conversion takes a little time, so we wait for it before loading into the list widget item
    # I think in an  ideal world this should be a BytesIO object rather than a file.
    # much easier to clean all that up at end of session

    sleep(2)
    self.thumb = (self.vidRoot + self.camvals["stillFormat"]) 
    self.myIcon = QtGui.QIcon(self.thumb) 
    self.myItem = QtWidgets.QListWidgetItem(self.myIcon, self.vidRoot, self.ui.thumbnails)        
    # then add it to the widget

def setupVideoCapture(self):
    #print ("++++++++++++++++++++++++++++++++++++++++++" ,  dir(self))
    """ make all relevant settings appropriate for video capture """
    # make vlc media player
    #self.vlcObj = vlc.Instance()
    #self.media = None
    #self.mediaplayer = self.vlcObj.media_player_new()
    #self.is_paused = False
    # set resolution for video
    self.resolution = tuple(self.vidres)
    # adjust display area for video
    self.ui.imgContainer.resize(800,600)

def setupStillCapture(self):
    #print(self)
    """ make all relevant settings for still capture """
    # set resolution for still
    self.resolution = tuple(self.imgres)
    # adjust display area for video
    self.ui.imgContainer.resize(self.resolution[0]/2, self.resolution[1]/2)

