"""
Contains some global functions for the cameraApp
"""
import pprint
import json
import io
from picamera import PiCamera
from fractions import Fraction

def getSettingsFile(camera):
    # print("In  settings File!")
    try:
        with open("settings.ini", "r") as settings:
            parmsDict = settings.read()
            # print(parmsDict)
            return parmsDict
            # now pass all the settings to the camera
            # and also set all the controls on the gui

    except:
        # define custom parameters
        parmsDict = {}
        customParms = {
            "stillFileRoot": "img_",
            "vidFileRoot": "vid_",
            "stillFormat": "jpeg",
            "videoFormat": "h264",
            "fileCounter": 41,
            "vidres": [
                1600,
                900
            ],
            "imgres": [
                1600,
                1200
            ]
        }
        # get the cameras parms
        parms = dir(camera)
        for i in parms:
            try:
                # get rid of private functions
                if i[0] != "_":
                    if str(getattr(camera, i))[0] != "<":
                        parmsDict.update({str(i): getattr(camera, i)})

            except:
                pass
        # add the custom parms to the camera parms
        parmsDict.update(customParms)
        # pretty print the parms to a str stream object
        # then put this to file
        parmsDictAsStream = io.StringIO("")
        pprint.pprint(parmsDict, parmsDictAsStream)
        settings = open("settings.ini", "w")
        settings.write(str(parmsDictAsStream.getvalue()))
    return parmsDict

#camera = PiCamera()
#x = getSettingsFile(camera)
# print(x)


