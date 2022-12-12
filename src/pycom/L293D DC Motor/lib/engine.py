import machine
from machine import PWM
from machine import Pin

pwm = PWM(0, frequency=50)
pwm_c = pwm.channel(0, pin='P12', duty_cycle=1)
dir1 = Pin('P23', mode=Pin.OUT)
dir2 = Pin('P22', mode=Pin.OUT)

def drive(val):
    print(val)
    # 472 // 479
    if(val > 479):
        percentage = (val - 479) / (1023 - 479);
        dir1.value(True)
        dir2.value(False)
    else:
        percentage = 1 - (val / 479)
        dir1.value(False)
        dir2.value(True)

    pwm_c.duty_cycle(percentage) # change the duty cycle to 30%
