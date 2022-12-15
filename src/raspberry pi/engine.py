import RPi.GPIO as GPIO
from time import sleep

m1_dir1 = 3
m2_dir1 = 15

m1_dir2 = 5
m2_dir2 = 13

m1_enable = 7
m2_enable = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(m1_dir1, GPIO.OUT)
GPIO.setup(m1_dir2, GPIO.OUT)
GPIO.setup(m2_dir1, GPIO.OUT)
GPIO.setup(m2_dir2, GPIO.OUT)

GPIO.setup(m1_enable, GPIO.OUT)
GPIO.setup(m2_enable, GPIO.OUT)

pwm=GPIO.PWM(m1_enable, 100)
pwm2=GPIO.PWM(m2_enable, 100)

pwm.start(0)
pwm2.start(0)
GPIO.output(m1_enable, True)
GPIO.output(m2_enable, True)

def drive(speed):
    # 472 // 479
    if(speed > 479):
        percentage = ((speed - 479) / (1023 - 479)) * 100
        GPIO.output(m1_dir1, True)
        GPIO.output(m1_dir2, False)
        GPIO.output(m2_dir1, True)
        GPIO.output(m2_dir2, False)
    else:
        percentage = (1 - (speed / 479)) * 100
        GPIO.output(m1_dir1, False)
        GPIO.output(m1_dir2, True)
        GPIO.output(m2_dir1, False)
        GPIO.output(m2_dir2, True)

    pwm.ChangeDutyCycle(percentage) # change the duty cycle
    pwm2.ChangeDutyCycle(percentage) # change the duty cycle