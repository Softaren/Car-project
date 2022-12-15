import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

def read_joystick():
    line = ser.readline()   # read a byte
    if line:
        pos = line.decode()  # convert the byte string to a unicode string
        return pos