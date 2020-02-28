import serial  # https://pyserial.readthedocs.io/en/latest/pyserial.html
from time import sleep

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    print('>')
    s.write(b'foo')
    print('<')
    sleep(5)
    pending = s.in_waiting
    print(pending)
    if pending:
        print(s.read(pending).decode('utf-8').strip())
