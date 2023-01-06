import socket as s
from engine import drive
from steering import steer
 
UDP_IP = "192.168.2.8"
UDP_PORT = 65432

def is_connected():
    try:
        print("Checking network")
        s.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

while True:
    if(is_connected()):
        sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
        sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        sock.bind((UDP_IP, UDP_PORT))

        print("Listening... on ", UDP_IP, " with port ", UDP_PORT)
        break


def wait_for_controller_commands():
    while True:
        data, addr = sock.recvfrom(2048)
        (c, x_value, y_value) = data.decode('utf-8').split('|')
        drive(c, float(y_value))
        steer(c, float(x_value))

        