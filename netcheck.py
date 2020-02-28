import socket
import random
import sys
import signal
from sense_hat import SenseHat
from time import sleep


targets = [
    ('54.76.20.121', 80),
    ('8.8.8.8', 53),
    ('8.8.4.4', 53),
]

statusOk = False
red = (255, 0, 0)
green = (0, 255, 0)
_ = (0, 0, 0)
sense = SenseHat()
sense.set_rotation(180)
gray = (80, 80, 80)


def drawLogo(c):
    logo = [
        _, _, c, c, c, c, _, _,
        _, c, _, _, _, _, c, _,
        c, _, _, c, c, _, _, c,
        _, _, c, _, _, c, _, _,
        _, c, _, _, _, _, c, _,
        _, _, _, c, c, _, _, _,
        _, _, _, _, _, _, _, _,
        _, _, _, c, c, _, _, _,
    ]
    sense.set_pixels(logo)


def drawPending(c):
    logo = [
        _, _, c, c, c, _, _, _,
        _, c, _, _, _, c, _, _,
        _, c, _, _, _, c, _, _,
        _, _, _, _, c, _, _, _,
        _, _, _, c, _, _, _, _,
        _, _, _, c, _, _, _, _,
        _, _, _, _, _, _, _, _,
        _, _, _, c, _, _, _, _,
    ]
    sense.set_pixels(logo)


def signalHandler(sig, frame):
    sense.clear()
    print('Shutting down netcheck.py')
    exit(0)


quiet = '-q' in sys.argv
displayColor = gray

signal.signal(signal.SIGINT, signalHandler)

while True:
    target = random.choice(targets)
    sense.clear()
    drawPending(displayColor)
    try:
        s = socket.create_connection(target, 10)
        statusOk = True
        s.close()
    except Exception:
        statusOk = False

    displayColor = green if statusOk else red
    drawLogo(displayColor)
    if not quiet:
        print(target[0], end=" ")
        print('.' if statusOk else 'x')
    sleep(60)
