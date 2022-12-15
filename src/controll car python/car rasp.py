import socket
from joystick import read_joystick

UDP_IP = "192.168.2.121"
UDP_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        (Y_value, X_value) = read_joystick().split("|")
        
        s.sendto(str.encode("\n".join([str(Y_value.rstrip()), str(X_value.rstrip())])), (UDP_IP, UDP_PORT))