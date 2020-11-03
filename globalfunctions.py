"""
Contains some global functions for the cameraApp
"""
import pprint
import json
import io
import os
#from picamera import PiCamera
import defaultcamerasettings as dcs
from fractions import Fraction

def getSettingsFile(camera):
    #print("In  settings File!")
    if os.path.isfile("settings.json"):
        #print ("found settings file")
        pass
        try:
            with open("settings.json", "r") as f:
                x = f.read()
                #print("json: ", json.loads(x))
                parmsDict = json.loads(x)
                f.close()
                #print(parmsDict)
            return parmsDict
        except:
            pass
            #print("failed to load settings.json!")
            # now pass all the settings to the camera
            # and also set all the controls on the gui
    else:
        # define custom parameters
        #print ("somehow in else?")
        parmsDict = dcs.defaultCameraSettings
        parmsDict.update(dcs.defaultCustomSettings)
        ##print(parmsDict)
        x = json.dumps(parmsDict)
        with open('settings.json', 'w') as f:
            f.write(x)
            f.close()
        return parmsDict

#camera = PiCamera()
#x = getSettingsFile(camera)
##print(x)


