import usocket
import _thread
from engine import drive
import time

# Thread for handling a client
def client_thread(clientsocket,n):
    while True:
        try:
            # Receive maxium of 12 bytes from the client
            msg_size = clientsocket.recv(1).decode('UTF-8')

            # If recv() returns with 0 the other end closed the connection
            if len(msg_size) == 0:
                clientsocket.close()
                return
            else:
                # Do something wth the received data...
                r = clientsocket.recv(int(msg_size)).decode('UTF-8')
                if len(r) != 0:
                    rs = int(r)
                    drive(rs)
                time.sleep_ms(10)
        except:
            clientsocket.close()

# Set up server socket
serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
serversocket.bind(("192.168.2.217", 65432))

# Accept maximum of 5 connections at the same time
serversocket.listen(1)

def search_for_controller():
    print("Waiting for controller...")
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Start a new thread to handle the client
    _thread.start_new_thread(client_thread, (clientsocket, 0))
    print("Controller found!")
