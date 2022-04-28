import machine
import PicoRobotics
motorControl=PicoRobotics.KitronikPicoRobotics()
adc1=machine.ADC(28)
adc2=machine.ADC(26)
threshold=11
vL=5
vR=5
while True:
    sensR=adc1.read_u16()/1000
    sensL=adc2.read_u16()/1000
    if sensR>=threshold:
        vL=40
        vR=10
    elif sensL>=threshold:
        vL=10
        vR=40
    elif sensL<threshold and sensR<threshold:
        vL=20
        vR=20
    elif sensL>=threshold and sensR>=threshold:
        vL=20
        vR=20
    motorControl.motorOn(2,"f",vL)
    motorControl.motorOn(1,"f",vR)
    