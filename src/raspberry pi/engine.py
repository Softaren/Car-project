import RPi.GPIO as GPIO
from time import sleep
from distance import distance

joystick_middle = 498   #The middle point for the joystick used

m1_backwards = 3
m2_backwards = 15

m1_forwards = 5
m2_forwards = 13

m1_enable = 7
m2_enable = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(m1_backwards, GPIO.OUT)
GPIO.setup(m1_forwards, GPIO.OUT)
GPIO.setup(m2_backwards, GPIO.OUT)
GPIO.setup(m2_forwards, GPIO.OUT)

GPIO.setup(m1_enable, GPIO.OUT)
GPIO.setup(m2_enable, GPIO.OUT)

pwm=GPIO.PWM(m1_enable, 100)
pwm2=GPIO.PWM(m2_enable, 100)

pwm.start(0)
pwm2.start(0)

def scale_joystick_value(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def drive_backwards(controller, speed):
    if(controller == "j"):
        percentage = ((speed - joystick_middle) / (1023 - joystick_middle)) * 100
    else:
        percentage = round(scale_joystick_value(speed, (0, +1), (0, 100)), 2)

    GPIO.output(m1_backwards, True)
    GPIO.output(m1_forwards, False)
    GPIO.output(m2_backwards, True)
    GPIO.output(m2_forwards, False)

    pwm.ChangeDutyCycle(percentage)
    pwm2.ChangeDutyCycle(percentage)

def drive_forwards(controller, speed):
    if(controller == "j"):
        percentage = (1 - (speed / joystick_middle)) * 100
    else:
        percentage = round(scale_joystick_value(speed, (0, -1), (0, 100)), 2)
        
    GPIO.output(m1_backwards, False)
    GPIO.output(m1_forwards, True)
    GPIO.output(m2_backwards, False)
    GPIO.output(m2_forwards, True)

    pwm.ChangeDutyCycle(percentage)
    pwm2.ChangeDutyCycle(percentage)


def drive(controller, speed):
    if(distance() < 40):
        drive_backwards("a", 0.5) #Drive backwards at half speed
        sleep(1)
        return

    #Stop motors at stand still
    if((speed == 0 and controller == "a") or speed == joystick_middle):
        pwm.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        return
    
    if((speed > 0 and controller == "a") or speed > joystick_middle):
        drive_backwards(controller, speed)
    else:
        drive_forwards(controller, speed)