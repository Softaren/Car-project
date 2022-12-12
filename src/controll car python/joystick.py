import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

def read_joystick():

    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        return num