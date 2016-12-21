"""
hello world with led matrix
https://github.com/rm-hull/max7219

"""

import max7219.led as led

device = led.matrix()
device.show_message("Hello world!")
