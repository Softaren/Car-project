import RPi.GPIO as GPIO
from time import sleep

dir1 = 3
dir2 = 5
enable = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(dir1, GPIO.OUT)
GPIO.setup(dir2, GPIO.OUT)

GPIO.setup(enable, GPIO.OUT)

pwm=GPIO.PWM(enable, 100)

pwm.start(0)
GPIO.output(enable, True)

def drive(speed):
    # 472 // 479
    if(speed > 479):
        percentage = ((speed - 479) / (1023 - 479)) * 100
        GPIO.output(3, True)
        GPIO.output(5, False)
    else:
        percentage = (1 - (speed / 479)) * 100
        GPIO.output(3, False)
        GPIO.output(5, True)

    pwm.ChangeDutyCycle(percentage) # change the duty cycle