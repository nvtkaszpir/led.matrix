"""
hello world with led matrix
https://github.com/rm-hull/max7219

"""

import max7219.led as led
import time
device1 = led.matrix(cascaded=2)
device1.brightness(0) # min 0..15 max
#device.orientation(0) # from ethenet to leds
#device.orientation(90) # towards hdmi
#device.orientation(180) # towards eth
#device.orientation(270) # from hdmi

# fill square closer to usb, then closer to led

X=16
Y=8
for x in range(X):
    print x
    for y in range(Y):
	print " ", y
	device1.pixel(x,y,1)
	time.sleep(0.05)
