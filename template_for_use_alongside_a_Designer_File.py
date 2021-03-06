from PyQt5 import QtCore, QtGui, QtWidgets
"""
MainWindow.ui is a file initially created in QtDesigner.  This file is then translated into
a single Python class called Ui_MainWindow by pyuic5.

(substitue MainWindow for the name you gave the Dialo or MianWindow object in Designer)
"""
from camera2 import *


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
    ui = Ui_MainWindow()
    # pass a reference to the MainWindow object to the setupUi method of the Ui_MainWindow instance ui
    ui.setupUi(MainWindow)
    # show it!
    MainWindow.show()
    sys.exit(app.exec_())


