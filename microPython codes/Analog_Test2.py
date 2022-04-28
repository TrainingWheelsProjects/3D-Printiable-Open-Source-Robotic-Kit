import machine
import utime
adc1 = machine.ADC(28)
adc2 = machine.ADC(26)
while True:
    
    print(("Right:"),(adc1.read_u16()/1000),("Left:"),(adc2.read_u16()/1000))
    utime.sleep(0.2)