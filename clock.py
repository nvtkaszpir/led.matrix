#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import (
    proportional,
    CP437_FONT,
    TINY_FONT,
    SINCLAIR_FONT,
    LCD_FONT,
)

contrast = 8  # 0..16
font = TINY_FONT


def loop(
    n,
    block_orientation,
    rotate,
    inreverse,
    time_format="%H:%M",
    no_zero=True,
    font=font,
):
    print("Initializing device")
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=n or 1,
        block_orientation=block_orientation,
        rotate=rotate or 0,
        blocks_arranged_in_reverse_order=inreverse,
    )

    print("Starting infinite loop")
    while True:
        now = datetime.datetime.now()
        msg_time = now.strftime(time_format)

        # convert first zero to space, notice that %-H produces hours without spaces
        if no_zero and (msg_time[0] == "0"):
            msg = " " + msg_time[1:]
        else:
            msg = msg_time

        # draw each letter separately, to allow to have colon sign
        # still, hours are more squeezed than minutes for readibility
        with canvas(device) as draw:
            text(draw, (0, 0), msg[0], fill="white", font=proportional(font))
            text(draw, (3, 0), msg[1], fill="white", font=proportional(font))
            text(draw, (7, 0), msg[2], fill="white", font=proportional(font))
            text(draw, (9, 0), msg[3], fill="white", font=proportional(font))
            text(draw, (13, 0), msg[4], fill="white", font=proportional(font))
        device.contrast(contrast)
        time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="matrix_demo arguments",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--cascaded",
        "-n",
        type=int,
        default=2,
        help="Number of cascaded MAX7219 LED matrices",
    )
    parser.add_argument(
        "--block-orientation",
        type=int,
        default=90,
        choices=[0, 90, -90],
        help="Corrects block orientation when wired vertically",
    )
    parser.add_argument(
        "--rotate",
        type=int,
        default=2,
        choices=[0, 1, 2, 3],
        help="Rotate display 0=0°, 1=90°, 2=180°, 3=270°",
    )
    parser.add_argument(
        "--reverse-order",
        type=bool,
        default=False,
        help="Set to true if blocks are in reverse order",
    )

    parser.add_argument(
        "--time-format", type=str, default="%H:%M", help="Time format to use"
    )
    parser.add_argument(
        "--no-zero",
        type=bool,
        default=True,
        help="Remove zero from hour, so that '08:12' becomes ' 8:12'",
    )

    args = parser.parse_args()

    try:
        loop(
            args.cascaded,
            args.block_orientation,
            args.rotate,
            args.reverse_order,
            args.time_format,
            args.no_zero,
        )
    except KeyboardInterrupt:
        pass
