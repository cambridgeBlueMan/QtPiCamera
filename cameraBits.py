"""
mainly a documentation file. Lists most camera parms, what they are and their ranges
"""
from picamera import PiCamera

camera = PiCamera()
""" 
             camera_num: int = 0,
             stereo_mode: str = 'none',
             stereo_decimate: bool = False,
             resolution: Optional[{width, height}] = None,
             framerate: Any = None,
             sensor_mode: int = 0,
             led_pin: Any = None,
             clock_mode: str = 'reset',
             framerate_range: Any = None) -> Any
"""
# print(camera.camera_num) # doesn't appear to exist, can only be set on instantiation
# print(camera.stereo_mode) and decimate only for dual cams on compute modules
""" The sensor_mode, resolution, framerate, framerate_range, and clock_mode parameters provide 
initial values for the sensor_mode, resolution, framerate, framerate_range, and clock_mode 
attributes of the class (these attributes are all relatively expensive to set individually, 
hence setting them all upon construction is a speed optimization). 
"""
"""
sensor modes are a series of discrete resolution/framerate combinations
"""
print(camera.sensor_mode) #
print(camera.resolution) # implement for v1
print(camera.framerate) # implement for v1
print(camera.framerate_range) # check this updates on change of framerate
print(camera.framerate_delta)
"""
Retrieves or sets the mode of the camera's clock.
This is an advanced property which can be used to control the nature of the frame timestamps available from 
the frame property. When this is "reset" (the default) each frame's timestamp will be relative to the start of 
the recording. When this is "raw", each frame's timestamp will be relative to the last initialization of the camera.
The initial value of this property can be specified with the clock_mode parameter in the PiCamera constructor, 
and will default to "reset" if not specified."""
print(camera.clock_mode)

#print(camera.frame) # only gettable when camera is recording
"""
Retrieves the current analog gain of the camera.
When queried, this property returns the analog gain currently being used by the camera. 
The value represents the analog gain of the sensor prior to digital conversion. 
The value is returned as a ~fractions.Fraction instance. """
print(camera.analog_gain)


"""
Retrieves the current digital gain of the camera.
When queried, this property returns the digital gain currently being used by the camera. 
The value represents the digital gain the camera applies after conversion of the sensor's analog output. 
The value is returned as a ~fractions.Fraction instance.
"""
print(camera.digital_gain)
"""



Gets or sets the auto-white-balance gains of the camera.
When queried, this attribute returns a tuple of values representing the (red, blue) balance of the camera. The red and 
blue values are returned ~fractions.Fraction instances. The values will be between 0.0 and 8.0.
When set, this attribute adjusts the camera's auto-white-balance gains. The property can be specified as a single 
value in which case both red and blue gains will be adjusted equally, or as a (red, blue) tuple. Values can be 
specified as an int  , :ref:`float  ` or ~fractions.Fraction and each gain must be between 0.0 and 8.0. 
Typical values for the gains are between 0.9 and 1.9. The property can be set while recordings or previews are in 
progress.
Note
This attribute only has an effect when awb_mode is set to 'off'. Also note that even with AWB disabled, 
some attributes (specifically still_stats and drc_strength) can cause AWB re-calculations."""
print(camera.awb_gains)
print(camera.awb_mode) # got from AWB_MODES


# not interested in v1
print(camera.still_stats)
# retrieves or sets the synamic range compression. values held in DRC_STRENGTHS
print(camera.drc_strength)

"""
Retrieves or sets the brightness setting of the camera.
When queried, the brightness property returns the brightness level of the camera as an integer between 0 and 100. 
When set, the property adjusts the brightness of the camera. Brightness can be adjusted while previews or recordings 
are in progress. The default value is 50."""
print(camera.brightness)


print(camera.sharpness) #= 0, -100 to 100
print(camera.contrast) #= 0, -100 to 100
print(camera.saturation) #= 0, -100 to 100

"""
Retrieves or sets the apparent ISO setting of the camera.
When queried, the iso property returns the ISO setting of the camera, a value which represents the sensitivity of the 
camera to light . Lower values (e.g. 100) imply less sensitivity than higher values (e.g. 400 or 800). Lower 
sensitivities tend  to produce less "noisy" (smoother) images, but operate poorly in low light conditions.
When set, the property adjusts the sensitivity of the camera (by adjusting the analog_gain and digital_gain). 
Valid values are between 0 (auto) and 1600. The actual value used when iso is explicitly set will be one of the 
following values (whichever is closest): 100, 200, 320, 400, 500, 640, 800.
On the V1 camera module, non-zero ISO values attempt to fix overall gain at various levels. For example, ISO 100 
attempts to provide an overall gain of 1.0, ISO 200 attempts to provide overall gain of 2.0, etc. The algorithm 
prefers analog gain over digital gain to reduce noise.
On the V2 camera module, ISO 100 attempts to produce overall gain of ~1.84, and ISO 800 attempts to produce overall 
gain of ~14.72 (the V2 camera module was calibrated against the ISO film speed  standard).
The attribute can be adjusted while previews or recordings are in progress. The default value is 0 which means 
automatically determine a value according to image-taking conditions.
Note
Some users on the Pi camera forum have noted that higher ISO values than 800 (specifically up to 1600) can be 
achieved in certain conditions with exposure_mode set to 'sports' and iso set to 0. It doesn't appear to be possible 
to manually request an ISO setting higher than 800, but the picamera library will permit settings up to 1600 in case 
the underlying firmware permits such settings in particular circumstances.
Note
Certain exposure_mode values override the ISO setting. For example, 'off' fixes analog_gain and digital_gain 
entirely, preventing this property from adjusting them when set."""
print(camera.iso) # = 0 # auto

print(camera.video_stabilization) #= False

# EXPOSURE
"""
Retrieves the current shutter speed of the camera.

When queried, this property returns the shutter speed currently being used by the camera. If you have set 
shutter_speed to a non-zero value, then exposure_speed and shutter_speed should be equal. However, if shutter_speed 
is set to 0 (auto), then you can read the actual shutter speed being used from this attribute. The value is returned 
as an integer representing a number of microseconds. This is a read-only property."""
print(camera.exposure_speed)
print(camera.exposure_compensation) #= 0, -25 to 25


"""
Retrieves or sets the shutter speed of the camera in microseconds.

When queried, the shutter_speed property returns the shutter speed of the camera in microseconds, or 0 which 
indicates that the speed will be automatically determined by the auto-exposure algorithm. Faster shutter times 
naturally require greater amounts of illumination and vice versa.

When set, the property adjusts the shutter speed of the camera, which most obviously affects the illumination of 
subsequently captured images. Shutter speed can be adjusted while previews or recordings are running. The default 
value is 0 (auto).

Note

You can query the exposure_speed attribute to determine the actual shutter speed being used when this attribute is 
set to 0. Please note that this capability requires an up to date firmware (#692 or later).

Note

In later firmwares, this attribute is limited by the value of the framerate attribute. For example, if framerate is 
set to 30fps, the shutter speed cannot be slower than 33,333µs (1/fps)."""
print(camera.shutter_speed)


"""
Retrieves or sets the exposure mode of the camera.

When queried, the exposure_mode property returns a string representing the exposure setting of the camera. 
The possible values can be obtained from the PiCamera.EXPOSURE_MODES attribute, and are as follows:

'off'
'auto'
'night'
'nightpreview'
'backlight'
'spotlight'
'sports'
'snow'
'beach'
'verylong'
'fixedfps'
'antishake'
'fireworks'

When set, the property adjusts the camera’s exposure mode. The property can be set while recordings or previews are in 
progress. The default value is 'auto'.

Note

Exposure mode 'off' is special: this disables the camera’s automatic gain control, fixing the values of digital_gain 
and analog_gain.

Please note that these properties are not directly settable (although they can be influenced by setting iso prior to 
fixing the gains), and default to low values when the camera is first initialized. Therefore it is important to let 
them settle on higher values before disabling automatic gain control otherwise all frames captured will appear black.
"""
print(camera.exposure_mode) #= 'auto' got from EXPOSURE_MODES

"""
Retrieves or sets the metering mode of the camera.

When queried, the meter_mode property returns the method by which the camera determines the exposure as one of the 
following strings:

'average'
'spot'
'backlit'
'matrix'

When set, the property adjusts the camera’s metering mode. All modes set up two regions: a center region, and an 
outer region. The major difference between each mode is the size of the center region. The 'backlit' mode has the 
largest central region (30% of the width), while 'spot' has the smallest (10% of the width).

The property can be set while recordings or previews are in progress. The default value is 'average'. All possible 
values for the attribute can be obtained from the PiCamera.METER_MODES attribute."""
print(camera.meter_mode) #= 'average' got from METER_MODES

# got from flash modes dictionary
print(camera.flash_mode)

# got from imaage effects dictionary
print(camera.image_effect)# = 'none'
"""
Retrieves or sets the parameters for the current :attr:`effect  `.
When queried, the image_effect_params property either returns None (for effects which have no configurable parameters, 
or if no parameters have been configured), or a tuple of numeric values up to six elements long.
When set, the property changes the parameters of the current effect   as a sequence of numbers, or a single number. 
Attempting to set parameters on an effect which does not support parameters, or providing an incompatible set of parameters for an effect will raise a PiCameraValueError exception.
The effects which have parameters, and what combinations those parameters can take is as follows:
     
Effect
Parameters
Description
'solarize'
yuv, x0, y1, y2, y3
yuv controls whether data is processed as RGB (0) or YUV(1). Input values from 0 to x0 - 1 are remapped linearly 
onto the range 0 to y0. Values from x0 to 255 are remapped linearly onto the range y1 to y2.
x0, y0, y1, y2
Same as above, but yuv defaults to 0 (process as RGB).
yuv
Same as above, but x0, y0, y1, y2 default to 128, 128, 128, 0 respectively.
'colorpoint'
quadrant
quadrant specifies which quadrant of the U/V space to retain chroma from: 0=green, 1=red/yellow, 2=blue, 3=purple. 
There is no default; this effect does nothing until parameters are set.
'colorbalance'
lens, r, g, b, u, v
lens specifies the lens shading strength (0.0 to 256.0, where 0.0 indicates lens shading has no effect). r, g, b a
re multipliers for their respective color channels (0.0 to 256.0). u and v are offsets added 
 to the U/V plane (0 to 255).
lens, r, g, b
Same as above but u are defaulted to 0.
lens, r, b
Same as above but g also defaults to to 1.0.
'colorswap'
dir
If dir is 0, swap RGB to BGR. If dir is 1, swap RGB to BRG.
'posterise'
steps
Control the quantization steps for the image. Valid values are 2 to 32, and the default is 4.
'blur'
size
Specifies the size of the kernel. Valid values are 1 or 2.
'film'
strength, u, v
strength specifies the strength of effect. u and v are offsets added to the U/V plane (0 to 255).
'watercolor'
u, v
u and v specify offsets to add to the U/V plane (0 to 255).
 
No parameters indicates no U/V effect.
Accessor kind:
Getter
"""
print(camera.image_effect_params)



"""
Retrieves or sets the current color effect applied by the camera.
When queried, the color_effects property either returns None which indicates that the camera is using normal 
color settings, or a (u, v) tuple where u and v are integer values between 0 and 255.
When set, the property changes the color effect applied by the camera. The property can be set while recordings or 
previews are in progress. For example, to make the image black and white set the value to (128, 128). The default 
value is None."""
print(camera.color_effects)# = None

"""
Retrieves or sets whether denoise will be applied to image captures.
When queried, the image_denoise property returns a boolean value indicating whether or not the camera software will 
apply a denoise algorithm to image captures.
When set, the property activates or deactivates the denoise algorithm for image captures. The property can be set 
while recordings or previews are in progress. The default value is True.
"""
print(camera.image_denoise)

print(camera.video_denoise) # as above



print(camera.rotation)# = 0, 90, 180, 270

print(camera.hflip)
print(camera.vflip)# = False
print(camera.zoom) #= (0.0, 0.0, 1.0, 1.0)

imageFormat = ('jpeg', 'png', 'gif', 'bmp', 'yuv', 'rgb', 'rgba', 'bgr', 'bgra')
videoFormat = ('h264', 'mjpeg', 'yuv', 'rgb', 'rgba', 'bgr', 'bgra')

# preview
"""
preview resolution is set as an arg to show preview
so it is not a camera parm, but should be in the json
also, it would be useful for a preview size to be set as
a proportion of the current img or vid res
"""
# PREVIEW
print(camera.preview)
print(camera.preview_alpha)
print(camera.preview_layer)
print(camera.preview_fullscreen)
print(camera.preview_window)

# I think by default that

# not interested in preview overlays on preview for v1
print(camera.overlays) # a list of ovrlays, quite possible an empty list


# ANNOTATE
# background and foreground are colors
# annotations become part of the actual image file. unlike overlays, which are
# on the preview only

"""
Controls the color of the annotation text.
The annotate_foreground attribute specifies, partially, the color of the annotation text. The value is specified as a 
Color. The default is white.
Note
The underlying firmware does not directly support setting all components of the text color, only the Y' component 
of a Y'UV  tuple. This is roughly (but not precisely) analogous to the "brightness" of a color, so you may choose 
to think of this as setting how bright the annotation text will be relative to its background. In order to specify 
just the Y' component when setting this attribute, you may choose to construct the Color instance as follows:
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0)
"""
print(camera.annotate_foreground)
"""
Controls whether the current frame number is drawn as an annotation.
The annotate_frame_num attribute is a bool indicating whether or not the current frame number is rendered as an 
annotation, similar to annotate_text. The default is False.
"""
print(camera.annotate_frame_num)
"""
Retrieves or sets a text annotation for all output.
When queried, the annotate_text property returns the current annotation (if no annotation has been set, this is simply 
a blank string).
When set, the property immediately applies the annotation to the preview (if it is running) and to any future 
captures or video recording. Strings longer than 255 characters, or strings containing non-ASCII characters will 
raise a PiCameraValueError. The default value is ''.
"""
print(camera.annotate_text)
print(camera.annotate_text_size)
print(camera.annotate_background)

"""
there are options for both still capture and video capture.
I suspect that these need to be provided as part of the options 

"""
print(camera.led) # not relevant
print(camera.recording) # retruns whether reording or not bool
"""
Retrieves the system time according to the camera firmware.
The camera's timestamp is a 64-bit integer representing the number of microseconds since the last system boot. 
When the camera's clock_mode is 'raw' the values returned by this attribute are comparable to those from the frame 
~PiVideoFrame.timestamp attribute.
"""
print(camera.timestamp)
