class Ui_AdditionalSettings(object):
    """
    set appropriate ranges etc for compSlider and compDial widgets
    set initial values from camVals
    set self.camera values from camVals
    """
    def setParmsForWidgets(self, ui, camVals, camera):

        ui.brightness.setRanges(0,100,camVals["brightness"])
        ui.saturation.setRanges(-100,100,camVals["saturation"])
        ui.contrast.setRanges(-100,100,camVals["contrast"])
        ui.sharpness.setRanges(-100,100,camVals["sharpness"])

    def addItemsToCombos(selfself, ui, camVals, camera):
        """
        adds dictionary items drawn from the camera to the cobo boxes.

        bear in mind that this process triggers the currentIndexChanged signal, and thus
        triggers the setCamValFromCombo slot/routine

        This on initialisation will stet all the camVal indices for the comboBoxes
        to 0, and overwite the stored values.

        this means the setCamValFromCombo routine/slot must not activate until after initialisation 
        :return:
        """

        ui.awb_mode.addItems(camera.AWB_MODES)
        ui.clock_mode.addItems(camera.CLOCK_MODES)
        ui.drc_strength.addItems(camera.DRC_STRENGTHS)
        ui.exposure_mode.addItems(camera.EXPOSURE_MODES)
        ui.flash_mode.addItems(camera.FLASH_MODES)
        ui.image_effect.addItems(camera.IMAGE_EFFECTS)
        ui.meter_mode.addItems(camera.METER_MODES)
        # stereo mode is obscure and has currently been removed
        #ui.stereo_mode.addItems(camera.STEREO_MODES)
        ui.raw_format.addItems(camera.RAW_FORMATS)

        return True

    def setDefaultValueForCombos(self, ui, camVals, camera):

            #ui.awb_modes.setEditText(camVals["awb_modes"])
            #print("in widgetSettins!", camVals)
            ui.awb_mode.setCurrentIndex((self.getComboIndex(ui.awb_mode, camVals["awb_mode"])))
            ui.clock_mode.setCurrentIndex(self.getComboIndex(ui.clock_mode, camVals["clock_mode"]))
            ui.drc_strength.setCurrentIndex(self.getComboIndex(ui.drc_strength, camVals["drc_strength"]))
            ui.exposure_mode.setCurrentIndex(self.getComboIndex(ui.exposure_mode, camVals["exposure_mode"]))
            ui.flash_mode.setCurrentIndex(self.getComboIndex(ui.flash_mode, camVals["flash_mode"]))
            ui.image_effect.setCurrentIndex(self.getComboIndex(ui.image_effect, camVals["image_effect"]))
            ui.meter_mode.setCurrentIndex(self.getComboIndex(ui.meter_mode, camVals["meter_mode"]))
            #ui.stereo_mode.setCurrentIndex(self.getComboIndex(ui.stereo_mode, camVals["stereo_mode"]))
            ui.raw_format.setCurrentIndex(self.getComboIndex(ui.raw_format, camVals["raw_format"]))


        ##print(self.parent().parent().comboUpdate) # = True
    def getComboIndex(self, combo, camVal):
        """
        sets the currently selected combobox item to the val stored in camVals
        :param camVal:
        :return:
        """
        #print("camVal is: ", camVal)
        index = combo.findText(camVal)
        if index >= 0:
            #print("*****************************")
            #print(combo.currentText(), index)
            return index
        #else:
            # #print("not found!")


from mysliders import CompositeSlider
import resource_rc
