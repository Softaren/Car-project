import RPi.GPIO as GPIO
from time import sleep
from distance import distance

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


def scale_joystick_value(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def drive(c, speed):

    if(distance() < 40):
        if(speed < 0 or speed > 499):
            if(c == "j"):
                percentage = (1 - (speed / 499)) * 100
                GPIO.output(m1_dir1, False)
                GPIO.output(m1_dir2, True)
                GPIO.output(m2_dir1, False)
                GPIO.output(m2_dir2, True)
            else:
                percentage = round(scale_joystick_value(speed, (0, +1), (0, 100)), 2)
                GPIO.output(m1_dir1, True)
                GPIO.output(m1_dir2, False)
                GPIO.output(m2_dir1, True)
                GPIO.output(m2_dir2, False)
                sleep(1)
        return

    #Joystick middle
    print(speed)
    if((speed == 0 and c == "a") or speed == 498):
        pwm.ChangeDutyCycle(0) # change the duty cycle
        pwm2.ChangeDutyCycle(0) # change the duty cycle
        return

    # 472 // 479
    if(speed < 0 or speed > 499):
        if(c == "j"):
            percentage = ((speed - 499) / (1023 - 499)) * 100
            GPIO.output(m1_dir1, True)
            GPIO.output(m1_dir2, False)
            GPIO.output(m2_dir1, True)
            GPIO.output(m2_dir2, False)
        else:
            percentage = round(scale_joystick_value(speed, (0, -1), (0, 100)), 2)
            GPIO.output(m1_dir1, False)
            GPIO.output(m1_dir2, True)
            GPIO.output(m2_dir1, False)
            GPIO.output(m2_dir2, True)
    else:
        if(c == "j"):
            percentage = (1 - (speed / 499)) * 100
            GPIO.output(m1_dir1, False)
            GPIO.output(m1_dir2, True)
            GPIO.output(m2_dir1, False)
            GPIO.output(m2_dir2, True)
        else:
            percentage = round(scale_joystick_value(speed, (0, +1), (0, 100)), 2)
            GPIO.output(m1_dir1, True)
            GPIO.output(m1_dir2, False)
            GPIO.output(m2_dir1, True)
            GPIO.output(m2_dir2, False)


    pwm.ChangeDutyCycle(percentage) # change the duty cycle
    pwm2.ChangeDutyCycle(percentage) # change the duty cycle