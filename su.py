"""
hello world with led matrix
https://github.com/rm-hull/max7219

"""

import max7219.led as led
import time
device = led.matrix(cascaded=2)
device.brightness(0) # min 0..15 max
#device.orientation(0) # from ethenet to leds
#device.orientation(90) # towards hdmi
#device.orientation(180) # towards eth
#device.orientation(270) # from hdmi


device.flush()

X=16
Y=8
#device.letter(deviceId=0,asciiCode=65)
#time.sleep(0.05)

#device.letter(deviceId=1,asciiCode=66)
#time.sleep(0.05)


#device = led.matrix(cascaded=2, vertical=True)
#device.brightness(0) # min 0..15 max
device.orientation(270) # towards eth
device.show_message('Prawn Pedal', delay=0.05)


