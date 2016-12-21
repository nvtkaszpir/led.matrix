"""
https://github.com/rm-hull/max7219

"""

import max7219.led as led
import time


device = led.matrix(cascaded=2)
device.brightness(0) # min 0..15 max
device.orientation(270) # hdmi must be to the top
device.show_message(message, delay=0.05)


