"""
Two classes used to provide composite sliders. One as a dial the other as a horizontal slider.
Each slider has an associated spin box to show the current value. Updates to one control automatically
update the other control. values are then passed to the main window to allow camera settings to be made
and the settings dictionary to be updated
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class CompositeDial(qtw.QAbstractSlider):

    def __init__(self, parent):

        super().__init__(parent)
        # Main UI code goes here

        # set widget size
        self.setFixedSize(qtc.QSize(140,60))

        # make slider, set size
        self.slider = qtw.QDial(self)
        self.slider.setFixedSize((qtc.QSize(55,55)))
        # name slider (is this necessary?)
        self.slider.setObjectName("slider")

        # make spinbox, set size
        self.spinBox = qtw.QSpinBox(self)
        self.spinBox.setFixedSize((qtc.QSize(50, 45)))
        # position it
        self.spinBox.move(70,7)
        # name it. necessary?
        self.spinBox.setObjectName("spinBox")

        # connect signals and slots
        self.slider.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.slider.setValue)

        self.slider.valueChanged['int'].connect(self.doWork)
        self.spinBox.valueChanged['int'].connect(self.doWork)
        qtc.QMetaObject.connectSlotsByName(self)

        # show it
        self.show()
    
    def doWork(*args):
        args[0].parent().parent().updateCameraSettings(args[0].objectName(), args[1])
        pass

    def setRanges (self, min, max, default):

        self.spinBox.setMinimum(min)
        self.spinBox.setMaximum(max)
        self.spinBox.setValue(default)

        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setValue(default)


class CompositeSlider(qtw.QAbstractSlider):

    def __init__(self, parent):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__(parent)
        # Main UI code goes here

        # set widget size
        self.setFixedSize(qtc.QSize(230, 60))

        # make slider, set size
        self.slider = qtw.QSlider(self)
        self.slider.setFixedSize((qtc.QSize(155, 55)))
        self.slider.setOrientation(qtc.Qt.Horizontal)
        # name slider (is this necessary?)
        self.slider.setObjectName("slider")

        # make spinbox, set size
        self.spinBox = qtw.QSpinBox(self)
        self.spinBox.setFixedSize((qtc.QSize(50, 45)))
        # position it
        self.spinBox.move(170, 7)
        # name it. necessary?
        self.spinBox.setObjectName("spinBox")

        # connect signals and slots
        self.slider.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.slider.setValue)

        self.slider.valueChanged['int'].connect(self.doWork)
        self.spinBox.valueChanged['int'].connect(self.doWork)
        qtc.QMetaObject.connectSlotsByName(self)

        # show it
        self.show()

    def doWork(*args):
        # next line is far from satisfactory
        args[0].parent().parent().parent().parent().parent().parent().updateCameraSettings(args[0].objectName(), args[1])
        #print(args[0].parent().parent().parent().parent().parent().parent().objectName())
        #MainWindow.updateCameraSettings(args[0].objectName(), args[1])
        #print(dir(MainWindow))

        pass

    def setRanges(self, min, max, default):
        self.spinBox.setMinimum(min)
        self.spinBox.setMaximum(max)
        self.spinBox.setValue(default)

        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setValue(default)



class DDPlayerWindow(qtw.QLabel):                       # - QWidget    + QLabel
    def __init__(self, parent):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__(parent)
        self.setAcceptDrops(True)
        #self.setText(" Accept Drops")
        #self.setStyleSheet("QLabel { background-color : #ccd; color : blue; font-size: 20px;}")

    def dragEnterEvent(self, e):
        print("DragEnter")
        e.accept()

    def dragMoveEvent(self, e):
        print("DragMove")
        e.accept()

    def dropEvent(self, e):
        print("DropEvent")
        #print (type(e))
        #print(dir(e.mimeData().dumpObjectInfo()))
        #print(dir(e.mimeData().isWidgetType()))


        #print ("Mime data: ", e.mimeData())
        position = e.pos()
        print(position)
        print(e.mimeData().text())

        #self.setText(e.mimeData().text())                #  +++
        print(e.dropAction)
        e.setDropAction(qtc.Qt.MoveAction)                   #  +++

        e.accept()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = CompositeSlider()
    sys.exit(app.exec())
