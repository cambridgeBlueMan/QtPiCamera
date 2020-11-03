"""
This file contains two dictionaries, defaultCameraSettings and defaultCustomSettings

defaultCameraSettings is derived from dir(camera) and getattr(camera, i0) routines. Various
items are then removed in order to be able to create a useable json file. i.e. various class
types are removed

"""
import json
defaultCameraSettings = {
 'analog_gain': 0,
 'annotate_background': None,
 'annotate_frame_num': False,
 'annotate_text_size': 32,
 'awb_gains': (0,0),
 'awb_mode': 'auto',
 'brightness': 50,
 'clock_mode': 'reset',
 'closed': False,
 'color_effects': None,
 'contrast': 0,
 'crop': (0.0, 0.0, 1.0, 1.0),
 'digital_gain': 0,
 'drc_strength': 'off',
 'exposure_compensation': 0,
 'exposure_mode': 'auto',
 'exposure_speed': 0,
 'flash_mode': 'off',
 'framerate': (30, 1),
 'hflip': False,
 'image_denoise': True,
 'image_effect': 'none',
 'image_effect_params': None,
 'iso': 0,
 'meter_mode': 'average',
 'overlays': [],
 'preview': None,
 'preview_alpha': 255,
 'preview_fullscreen': True,
 'preview_layer': 2,
 'preview_window': None,
 'previewing': False,
 'raw_format': 'yuv',
 'recording': False,
 'resolution': (920, 1080),
 'rotation': 0,
 'saturation': 0,
 'sensor_mode': 0,
 'sharpness': 0,
 'shutter_speed': 0,
 'still_stats': False,
 'vflip': False,
 'video_denoise': True,
 'video_stabilization': False,
 'zoom': (0.0, 0.0, 1.0, 1.0)}

defaultCustomSettings = {
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
    ],
    "zStartX" : 0,
    "zStartY": 0,
    "zStartWidth": 0,
    "zStartHeight": 0,
    "zEndX" : 0,
    "zEndY": 0,
    "zEndWidth": 0,
    "zEndHeight": 0,
    "zoomX" : 0,
    "zoomY": 0,
    "zoomWidth": 0,
    "zoomHeight": 0
        }
# = open(twattock.json, "w")

#x = json.dumps(defaultCameraSettings)
#f = open("twattock.json", "w")
#f.write(x)
#f.close

#f = open("twattock.json", "r")
#x =f.read()
#f.close


#print(type(x))
#print(type(json.loads(x)))