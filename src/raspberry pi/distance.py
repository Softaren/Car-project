import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 35 
GPIO_ECHO = 31

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    
    return distance