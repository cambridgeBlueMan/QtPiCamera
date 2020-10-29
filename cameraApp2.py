# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.cameraApp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdditionalSettings(object):

    """
    set appropriate ranges etc for compSlider and compDial widgets
    set initial values from camVals
    set self.camera values from camVals
    """
    def setupUi2(self, ui, camVals, camera):
        ui.brightness.setRanges(0,100,camVals["brightness"])
        ui.saturation.setRanges(-100,100,0)
        ui.contrast.setRanges(-100,100,0)
        ui.sharpness.setRanges(-100,100,0)

        ui.awbModes.addItems(camera.AWB_MODES)
        ui.clockModes.addItems(camera.CLOCK_MODES)
        ui.drcStrengths.addItems(camera.DRC_STRENGTHS)
        ui.exposureModes.addItems(camera.EXPOSURE_MODES)
        ui.flashModes.addItems(camera.FLASH_MODES)
        ui.imageEffects.addItems(camera.IMAGE_EFFECTS)
        ui.meterModes.addItems(camera.METER_MODES)
        ui.stereoModes.addItems(camera.STEREO_MODES)
        ui.rawFormats.addItems(camera.RAW_FORMATS)

from mysliders import CompositeSlider
import resource_rc
