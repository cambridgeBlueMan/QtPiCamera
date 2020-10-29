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

        ui.awb_modes.addItems(camera.AWB_MODES)
        ui.clock_modes.addItems(camera.CLOCK_MODES)
        ui.drc_strengths.addItems(camera.DRC_STRENGTHS)
        ui.exposure_modes.addItems(camera.EXPOSURE_MODES)
        ui.flash_modes.addItems(camera.FLASH_MODES)
        ui.image_effects.addItems(camera.IMAGE_EFFECTS)
        ui.meter_modes.addItems(camera.METER_MODES)
        # stereo modes is obscure and has currently been removed
        #ui.stereo_modes.addItems(camera.STEREO_MODES)
        ui.raw_formats.addItems(camera.RAW_FORMATS)

        ui.awb_modes.setCurrentIndex(self.getComboIndex(ui.awb_modes, camVals["awb_mode"]))
        ui.clock_modes.setCurrentIndex(self.getComboIndex(ui.clock_modes, camVals["clock_mode"]))
        ui.drc_strengths.setCurrentIndex(self.getComboIndex(ui.drc_strengths, camVals["drc_strength"]))
        ui.exposure_modes.setCurrentIndex(self.getComboIndex(ui.exposure_modes, camVals["exposure_mode"]))
        ui.flash_modes.setCurrentIndex(self.getComboIndex(ui.flash_modes, camVals["flash_mode"]))
        ui.image_effects.setCurrentIndex(self.getComboIndex(ui.image_effects, camVals["image_effect"]))
        ui.meter_modes.setCurrentIndex(self.getComboIndex(ui.meter_modes, camVals["meter_mode"]))
        #ui.stereo_modes.setCurrentIndex(self.getComboIndex(ui.stereo_modes, camVals["stereo_mode"]))
        ui.raw_formats.setCurrentIndex(self.getComboIndex(ui.raw_formats, camVals["raw_format"]))

    def getComboIndex(self, combo, camVal):
        """
        sets the currently selected combobox item to the val stored in camVals
        :param camVal:
        :return:
        """
        index = combo.findText(camVal)
        if index >= 0:
            #print("done it!", index)
            return index
        #else:
            # print("not found!")


from mysliders import CompositeSlider
import resource_rc
