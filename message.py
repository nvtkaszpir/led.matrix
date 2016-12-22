"""
https://github.com/rm-hull/max7219

"""

import max7219.led as led
from max7219.font import CP437_FONT, SINCLAIR_FONT, LCD_FONT, UKR_FONT, TINY_FONT
import click

# fonts definitions from max7219.font
fonts = {
    'CP437_FONT': CP437_FONT,
    'SINCLAIR_FONT': SINCLAIR_FONT,
    'LCD_FONT': LCD_FONT,
    'UKR_FONT': UKR_FONT,
    'TINY_FONT':TINY_FONT,
}



@click.command()
@click.argument('message', required=1)
@click.option('--b', default=0, help='brightness level from 0 to 15, default 0 is very dim, above 7 is bright')
@click.option('--d', default=0.05, help='delay, fraction of second, defualt 0.05')
@click.option('--f', default='LCD_FONT', help='font to use: ' + ','.join(fonts.keys()))
def main(message, b, d, f):
    device = led.matrix(cascaded=2)
    device.brightness(b) # min 0..15 max
    device.orientation(270) # hdmi must be to the top
    device.show_message(text=message, delay=d, font=fonts[f])


if __name__ == '__main__':
    main()



