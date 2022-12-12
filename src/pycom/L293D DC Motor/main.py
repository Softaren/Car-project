from engine import drive
from controller import search_for_controller
import time


while True:
    search_for_controller()

    #drive()
    time.sleep_ms(10)
