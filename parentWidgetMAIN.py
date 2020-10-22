"""
Sketch file. Works in conjunction with mysliders to develop functionaity for composite sliders
"""
from PyQt5 import QtCore, QtGui, QtWidgets

"""
MainWindow.ui is a file initially created in QtDesigner.  This file is then translated into
a single Python class called Ui_MainWindow by pyuic5.

(substitue MainWindow for the name you gave the Dialo or MianWindow object in Designer)
"""
from picamera import PiCamera
from parentWidget import Ui_MainWindow
from globalfunctions import getSettingsFile

class Code_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.camera = PiCamera()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # update the ui with settings
        self.parmsDict = getSettingsFile(self.camera)
        # set the ranges for the various controls
        # eg contrast
        self.ui.contrast.setRanges(-100,100,0)
        self.ui.twattock.setRanges(-30,30,0)
        self.show()

    def updateCameraSettings(*args):
        # print the control name and its value
        print (args[1], args[2])
        # now look for it, if you find it then set the camewra and update the dictionary
        if args[1] in args[0].parmsDict:
            print("found it!")
        else:
            print("not there!")

    """
Add the additional methods/ data structures etc here
    def myClick(*args):
        print(args[0].sender().property("buttonVal"))



    """


if __name__ == "__main__":
    import sys

    # instiantiate an app object from the QApplication class
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_MainWindow()
    # instantiate an object from the imported Ui_MainWindow class
    # ui = Ui_MainWindow()
    # pass a reference to the MainWindow object to the setupUi method of the Ui_MainWindow instance ui
    # ui.setupUi(MainWindow)
    # show it!
    # MainWindow.show()
    sys.exit(app.exec_())


