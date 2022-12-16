import socket as s
from engine import drive
from steering import steer
 
UDP_IP = "192.168.2.121"
UDP_PORT = 65432

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

print("Listening... on ", UDP_IP, " with port ", UDP_PORT)


def wait_for_controller_commands():
    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
        (Y_value, X_value) = data.decode('utf-8').split('\n')
        drive(int(Y_value))
        steer(int(X_value))