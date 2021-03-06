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
G = (100, 100, 100)
_ = (0, 0, 0)
c = (60, 150, 240)
l = (40, 97, 240)
b = (0, 0, 255)
d = (0, 0, 140)
p = (180, 115, 75)
P = (160, 100, 70)
r = (200, 50, 50)
R = (255, 100, 100)

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
    ],
    'fish': [
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            l, _, _, _, _, _, _, _,
            b, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            l, _, _, _, _, _, _, _,
            _, l, _, _, _, _, _, _,
            b, b, _, _, _, _, _, _,
            b, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            l, _, _, _, _, _, _, _,
            b, l, _, _, _, _, _, _,
            _, g, l, _, _, _, _, _,
            b, b, b, _, _, _, _, _,
            b, b, _, _, _, _, _, _,
            d, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            l, l, _, _, _, _, _, _,
            b, b, l, _, _, _, _, _,
            b, _, g, l, _, _, _, _,
            l, b, b, b, _, _, _, _,
            b, b, b, _, _, _, _, _,
            d, d, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, l, l, _, _, _, _, _,
            b, b, b, l, _, _, _, _,
            b, b, _, g, l, _, _, _,
            l, l, b, b, b, _, _, _,
            d, b, b, b, _, _, _, _,
            _, d, d, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, l, l, _, _, _, _,
            _, b, b, b, l, _, _, _,
            b, b, b, _, g, l, _, _,
            b, l, l, b, b, b, _, _,
            _, d, b, b, b, _, _, _,
            _, _, d, d, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, l, l, _, _, _,
            l, _, b, b, b, l, _, _,
            b, b, b, b, _, g, l, _,
            b, b, l, l, b, b, b, _,
            d, _, d, b, b, b, _, _,
            _, _, _, d, d, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            l, _, _, _, l, l, _, _,
            b, l, _, b, b, b, l, _,
            d, b, b, b, b, _, g, l,
            d, b, b, l, l, b, b, b,
            b, d, _, d, b, b, b, _,
            d, _, _, _, d, d, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            l, _, _, _, l, l, _, _,
            b, l, _, b, b, b, l, _,
            b, b, b, b, b, g, _, l,
            b, b, b, l, l, b, b, b,
            b, d, _, d, b, b, b, _,
            d, _, _, _, d, d, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            l, _, _, _, l, l, _, _,
            b, l, _, b, b, b, l, _,
            d, b, b, b, b, _, g, l,
            d, b, b, l, l, b, b, b,
            b, d, _, d, b, b, b, _,
            d, _, _, _, d, d, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, l, _, _, _, l, l, _,
            _, b, l, _, b, b, b, l,
            _, d, b, b, b, b, _, g,
            _, d, b, b, l, l, b, b,
            _, b, d, _, d, b, b, b,
            _, d, _, _, _, d, d, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, l, _, _, _, l, l,
            _, _, b, l, _, b, b, b,
            _, _, d, b, b, b, b, _,
            _, _, d, b, b, l, l, b,
            _, _, b, d, _, d, b, b,
            _, _, d, _, _, _, d, d,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, l, _, _, _, l,
            _, _, _, b, l, _, b, b,
            _, _, _, d, b, b, b, b,
            _, _, _, d, b, b, l, l,
            _, _, _, b, d, _, d, b,
            _, _, _, d, _, _, _, d,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, l, _, _, _,
            _, _, _, _, b, l, _, b,
            _, _, _, _, d, b, b, b,
            _, _, _, _, d, b, b, l,
            _, _, _, _, b, d, _, d,
            _, _, _, _, d, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, l, _, _,
            _, _, _, _, _, b, l, _,
            _, _, _, _, _, d, b, b,
            _, _, _, _, _, d, b, b,
            _, _, _, _, _, b, d, _,
            _, _, _, _, _, d, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, l, _,
            _, _, _, _, _, _, b, l,
            _, _, _, _, _, _, d, b,
            _, _, _, _, _, _, d, b,
            _, _, _, _, _, _, b, d,
            _, _, _, _, _, _, d, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, l,
            _, _, _, _, _, _, _, b,
            _, _, _, _, _, _, _, d,
            _, _, _, _, _, _, _, d,
            _, _, _, _, _, _, _, b,
            _, _, _, _, _, _, _, d,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ]
    ],
    'eye': [
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, _, _, _, _, _, _, P,
            _, P, _, _, _, _, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, _, _, _, _, _, _, P,
            _, P, P, P, P, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, P, P, P, P, P, P, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, P, P, P, P, _, _,
            P, P, b, _, _, b, P, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, P, P, P, P, _, _,
            _, P, G, b, b, G, P, _,
            P, P, b, _, _, b, P, P,
            _, P, G, b, b, G, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        # [
        #     _, _, P, P, P, P, _, _,
        #     _, P, P, G, G, P, P, _,
        #     _, P, G, b, b, G, P, _,
        #     P, G, b, _, _, b, G, P,
        #     _, P, G, b, b, G, P, _,
        #     _, P, P, G, G, P, P, _,
        #     _, _, P, P, P, P, _, _,
        #     _, _, _, _, _, _, _, _,
        # ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, b, b, G, G, P,
            G, G, b, _, _, b, G, G,
            P, G, G, b, b, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, b, b, G, G, G, P,
            G, b, _, _, b, G, G, G,
            P, G, b, b, G, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, b, b, G, G, G, G, P,
            b, _, _, b, G, G, G, G,
            P, b, b, G, G, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, b, b, G, G, G, P,
            G, b, _, _, b, G, G, G,
            P, G, b, b, G, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, b, b, G, G, P,
            G, G, b, _, _, b, G, G,
            P, G, G, b, b, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, G, b, b, G, P,
            G, G, G, b, _, _, b, G,
            P, G, G, G, b, b, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, G, G, b, b, P,
            G, G, G, G, b, _, _, b,
            P, G, G, G, G, b, b, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, G, b, b, G, P,
            G, G, G, b, _, _, b, G,
            P, G, G, G, b, b, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, P, P, P, P, _, _,
            _, P, P, G, G, P, P, _,
            P, G, G, b, b, G, G, P,
            G, G, b, _, _, b, G, G,
            P, G, G, b, b, G, G, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, P, P, P, P, _, _,
            _, P, G, b, b, G, P, _,
            P, P, b, _, _, b, P, P,
            _, P, G, b, b, G, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, P, P, P, P, _, _,
            P, P, b, _, _, b, P, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, P, P, P, P, P, P, P,
            _, P, P, G, G, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, _, _, _, _, _, _, P,
            _, P, P, P, P, P, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            P, _, _, _, _, _, _, P,
            _, P, _, _, _, _, P, _,
            _, _, P, P, P, P, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ]
    ],
    'hearts': [
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, r, r, _, _, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, r, r, _, _, _,
            _, _, r, r, r, r, _, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, r, r, r, r, _, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, r, r, r, r, _, _,
            _, _, r, r, r, r, _, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
            _, _, _, _, _, _, _, _,
        ],
        [
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
        ],
        [
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            _, r, r, r, r, r, r, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
        ],
        [
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            r, r, r, r, r, r, r, r,
            r, r, r, _, _, r, r, r,
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
        ],
        [
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            r, r, r, _, _, r, r, r,
            r, r, _, _, _, _, r, r,
            _, r, _, _, _, _, r, _,
            _, r, r, _, _, r, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
        ],
        [
            _, r, r, _, _, r, r, _,
            _, r, r, r, r, r, r, _,
            r, r, _, _, _, _, r, r,
            r, r, _, _, _, _, r, r,
            _, r, _, _, _, _, r, _,
            _, r, _, _, _, _, r, _,
            _, _, r, r, r, r, _, _,
            _, _, _, r, r, _, _, _,
        ],
        [
            _, R, R, _, _, R, R, _,
            _, R, _, R, R, _, R, _,
            R, _, _, _, _, _, _, R,
            R, _, _, _, _, _, _, R,
            _, R, _, _, _, _, R, _,
            _, R, _, _, _, _, R, _,
            _, _, R, _, _, R, _, _,
            _, _, _, R, R, _, _, _,
        ],
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ]
    ],

    # For ease of copying:
    'blank': [
        [
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
            _, _, _, _, _, _, _, _,
        ]
    ],
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
    parser.add_argument('--duration', required=False, help='Duration in seconds', action='store', default=60, type=int)
    parser.add_argument('--keep', required=False, help='Don\'t clear screen', action='store_true')
    args = parser.parse_args()
    return args


def dim(matrix: List, multiplier: float) -> List:
    return [[math.floor(c * multiplier) for c in cell] for cell in matrix]


args = parse_cli_args()
image_name = args.image

if args.sim:
    SenseHat = SimHat
    brightness = 1
    target = 'sim'
else:
    SenseHat = RealHat
    brightness = 0.5
    target = 'hat'

print(f'Requested {image_name} in {target}')

sense = SenseHat()
sense.set_rotation(args.rotate)
duration = args.duration

if image_name in images:
    image = images[image_name]
    frame_count = len(image)
    if frame_count == 1:
        sense.set_pixels(dim(image[0], brightness))
        sleep(duration)
    else:
        for loop in range(1, math.floor(duration / (0.7 + (frame_count * 0.3)))):
            for frame in image:
                sense.set_pixels(dim(frame, brightness))
                sleep(0.3)
            sleep(0.7)

    if not args.keep:
        sense.clear()
else:
    raise Exception(f'Invalid image {image_name} requested')
