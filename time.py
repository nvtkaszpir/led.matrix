"""
https://github.com/rm-hull/max7219
24h clock tweked for tiny text 
"""

import max7219.led as led
from max7219.font import proportional, CP437_FONT, SINCLAIR_FONT, LCD_FONT, UKR_FONT, TINY_FONT

import datetime
import click
import time


# fonts definitions from max7219.font
fonts = {
    'CP437_FONT': CP437_FONT,
    'SINCLAIR_FONT': SINCLAIR_FONT,
    'LCD_FONT': LCD_FONT,
    'UKR_FONT': UKR_FONT,
    'TINY_FONT':TINY_FONT,
}



@click.command()
@click.option('--b', default=0, help='brightness level from 0 to 15, default 0 is very dim, above 7 is bright')
@click.option('--d', default=0.05, help='delay, fraction of second, defualt 0.05')
@click.option('--f', default='TINY_FONT', help='font to use: ' + ', '.join(fonts.keys()))
@click.option('--t', default="%H%M", help='time format, default %H%M')
def main(b, d, f, t):
    device = led.matrix(cascaded=2)
    device.clear()
    device.brightness(b) # min 0..15 max
    device.orientation(270) # hdmi must be to the top
    now = datetime.datetime.now()
    text = now.strftime(t)
    device.show_message(text=text, delay=d, font=proportional(fonts[f]))


if __name__ == '__main__':
    main()




