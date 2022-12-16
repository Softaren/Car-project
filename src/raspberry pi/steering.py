from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(13, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

def scale_joystick_value(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def steer(pos):
    #527
    percentage = round(scale_joystick_value(int(pos), (0.0, 1023.0), (-0.24, +0.23)), 2)
    servo.value = percentage