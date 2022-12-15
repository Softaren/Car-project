import socket
from joystick import read_joystick


HOST = "192.168.2.217"
PORT = 65432



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        val = read_joystick()

        size = str(len(str(val)))

        s.send(str(len(str(val))).encode('utf-8'))
        s.send(str(val).encode('utf-8'))