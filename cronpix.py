#!/usr/bin/env python3
"""
Display lo-res pix on demand
"""
import argparse
import math
from sense_hat import SenseHat as RealHat
from sense_emu import SenseHat as SimHat

from time import sleep
from typing import List


w = (225, 225, 225)
g = (150, 150, 150)
b = (0, 0, 255)
_ = (0, 0, 0)
c = (60, 150, 240)
p = (180, 115, 75)

images = {
    # 8x8
    'shower': [
        [
            w, w, w, _, w, _, _, _,
            w, _, _, w, _, c, _, _,
            w, _, w, c, _, _, c, _,
            w, _, _, _, c, _, _, _,
            w, _, c, _, _, _, _, _,
            w, _, c, _, _, _, c, _,
            w, _, _, _, _, _, _, _,
            w, _, _, _, _, _, _, _,
        ], [
            w, w, w, _, w, _, _, _,
            w, _, _, w, _, _, _, _,
            w, _, w, _, _, c, _, _,
            w, _, _, c, _, _, c, _,
            w, _, _, _, c, _, _, _,
            w, _, c, _, _, _, _, _,
            w, _, c, _, _, _, c, _,
            w, _, _, _, _, _, _, _,
        ], [
            w, w, w, _, w, _, _, _,
            w, _, _, w, _, _, _, _,
            w, _, w, _, _, _, _, _,
            w, _, _, _, _, c, _, _,
            w, _, _, c, _, _, c, _,
            w, _, _, _, c, _, _, _,
            w, _, c, _, _, _, _, _,
            w, _, c, _, _, _, c, _,
        ], [
            w, w, w, _, w, _, _, _,
            w, _, _, w, _, _, _, _,
            w, _, w, _, _, _, _, _,
            w, _, _, _, _, c, _, _,
            w, _, _, _, _, c, _, _,
            w, _, _, c, _, _, c, _,
            w, _, _, _, c, _, _, _,
            w, _, c, _, _, _, _, _,
        ], [
            w, w, w, _, w, _, _, _,
            w, _, _, w, _, _, _, _,
            w, _, w, _, _, _, _, _,
            w, _, _, _, _, _, _, _,
            w, _, _, _, _, c, _, _,
            w, _, _, _, _, c, _, _,
            w, _, _, c, _, _, c, _,
            w, _, _, _, c, _, _, _,
        ],
    ],

    'bed': [
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, p, _, _,
            _, _, _, _, _, b, _, _,
            g, _, _, _, _, b, _, _,
            g, _, _, _, _, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, p, _, _, _, _, _,
            g, _, _, b, _, _, _, _,
            g, _, _, _, b, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            g, _, _, _, _, _, _, _,
            g, _, p, b, b, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, w, _, _, _, _,
            g, _, _, _, _, _, _, _,
            g, _, p, b, b, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, w, _, _, _,
            _, _, _, w, _, _, _, _,
            g, _, _, _, _, _, _, _,
            g, _, p, b, b, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
        [
            _, _, _, _, _, g, w, _,
            _, _, _, _, g, g, g, g,
            _, _, _, _, _, w, g, _,
            _, _, _, _, _, _, _, _,
            g, _, _, _, _, _, _, _,
            g, _, p, b, b, b, b, _,
            g, g, g, g, g, g, g, g,
            g, _, _, _, _, _, _, g,
        ],
    ]
}


def parse_cli_args() -> argparse.Namespace:
    """
    Set up & parse CLI arguments

    Returns:
        Namespace of parsed args
    """
    parser = argparse.ArgumentParser(
        description='Display lo-res pix on demand',
    )
    parser.add_argument('image', help='image to display')
    parser.add_argument('--sim', required=False, help='Use the SenseHat simulator', action='store_true')
    parser.add_argument('--rotate', required=False, help='Set screen rotation', action='store', default=0, type=int)
    args = parser.parse_args()
    return args


def dim(matrix: List, multiplier: float) -> List:
    return [[math.floor(c * multiplier) for c in cell] for cell in matrix]


args = parse_cli_args()
target = 'SIM' if args.sim else 'LIVE'
image_name = args.image
print(f'Requested {image_name} in {target}')

if args.sim:
    SenseHat = SimHat
    brightness = 1
else:
    SenseHat = RealHat
    brightness = 0.5

sense = SenseHat()
sense.set_rotation(args.rotate)

if image_name in images:
    image = images[image_name]
    if len(image) == 1:
        sense.set_pixels(dim(image[0], brightness))
    else:
        for loop in range(1, 10):
            for frame in image:
                sense.set_pixels(dim(frame, brightness))
                sleep(0.3)
            sleep(0.7)

    sleep(30)
    sense.clear()
else:
    raise Exception(f'Invalid image {image_name} requested')
