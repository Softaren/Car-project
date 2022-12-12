import machine

adc = machine.ADC(bits=10)              # create an ADC object
apin = adc.channel(pin='P16', attn=machine.ADC.ATTN_11DB)   # create an analog pin on P16
val = apin()                    # read an analog value
