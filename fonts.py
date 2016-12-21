"""
hello world with led matrix
https://github.com/rm-hull/max7219

"""

import max7219.led as led
from max7219.font import CP437_FONT, SINCLAIR_FONT, LCD_FONT, UKR_FONT, TINY_FONT

fonts = {
    'CP437_FONT': CP437_FONT, 
    'SINCLAIR_FONT': SINCLAIR_FONT, 
    'LCD_FONT': LCD_FONT,
    'UKR_FONT': UKR_FONT,
    'TINY_FONT':TINY_FONT,
}

device = led.matrix()
device.brightness(0)
for f in fonts.keys():
    device.show_message(text=f, font=fonts[f])
