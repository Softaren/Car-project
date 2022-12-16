from controller import wait_for_controller_commands
#from threading import Thread

while True:

    wait_for_controller_commands()

    #controller_thread = Thread(target=wait_for_controller_commands)
    #controller_thread.start()