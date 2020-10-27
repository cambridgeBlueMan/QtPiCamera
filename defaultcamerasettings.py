"""
This file contains two dictionaries, defaultCameraSettings and defaultCustomSettings

defaultCameraSettings is derived from dir(camera) and getattr(camera, i0) routines. Various
items are then removed in order to be able to create a useable json file. i.e. various class
types are removed

"""
import json
defaultCameraSettings = {'AWB_MODES': {'auto': 1,
               'cloudy': 3,
               'flash': 8,
               'fluorescent': 6,
               'horizon': 9,
               'incandescent': 7,
               'off': 0,
               'shade': 4,
               'sunlight': 2,
               'tungsten': 5},
 'CAMERA_CAPTURE_PORT': 2,
 'CAMERA_PREVIEW_PORT': 0,
 'CAMERA_VIDEO_PORT': 1,
 'CAPTURE_TIMEOUT': 60,
 'CLOCK_MODES': {'raw': 1, 'reset': 2},
 'DEFAULT_ANNOTATE_SIZE': 32,
 'DRC_STRENGTHS': {'high': 3, 'low': 1, 'medium': 2, 'off': 0},
 'EXPOSURE_MODES': {'antishake': 11,
                    'auto': 1,
                    'backlight': 4,
                    'beach': 8,
                    'fireworks': 12,
                    'fixedfps': 10,
                    'night': 2,
                    'nightpreview': 3,
                    'off': 0,
                    'snow': 7,
                    'sports': 6,
                    'spotlight': 5,
                    'verylong': 9},
 'FLASH_MODES': {'auto': 1,
                 'fillin': 4,
                 'off': 0,
                 'on': 2,
                 'redeye': 3,
                 'torch': 5},
 'IMAGE_EFFECTS': {'blur': 15,
                   'cartoon': 22,
                   'colorbalance': 21,
                   'colorpoint': 20,
                   'colorswap': 17,
                   'deinterlace1': 23,
                   'deinterlace2': 24,
                   'denoise': 7,
                   'emboss': 8,
                   'film': 14,
                   'gpen': 11,
                   'hatch': 10,
                   'negative': 1,
                   'none': 0,
                   'oilpaint': 9,
                   'pastel': 12,
                   'posterise': 19,
                   'saturation': 16,
                   'sketch': 6,
                   'solarize': 2,
                   'washedout': 18,
                   'watercolor': 13},
 'ISO': 0,
 'MAX_FRAMERATE': 120,
 'MAX_RESOLUTION': (4056, 3040),
 'METER_MODES': {'average': 0, 'backlit': 2, 'matrix': 3, 'spot': 1},
 'RAW_FORMATS': ('rgb', 'yuv', 'rgba', 'bgra', 'bgr'),
 'STEREO_MODES': {'none': 0, 'side-by-side': 1, 'top-bottom': 2},
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
 'exif_tags': {'IFD0.Make': 'RaspberryPi', 'IFD0.Model': 'RP_imx477'},
 'exposure_compensation': 0,
 'exposure_mode': 'auto',
 'exposure_speed': 0,
 'flash_mode': 'off',
 'framerate': (30, 1),
 'framerate_delta': 0,
 'framerate_range': ((30, 1), (30, 1)),
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
 'revision': 'imx477',
 'rotation': 0,
 'saturation': 0,
 'sensor_mode': 0,
 'sharpness': 0,
 'shutter_speed': 0,
 'still_stats': False,
 'timestamp': 3129722522,
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