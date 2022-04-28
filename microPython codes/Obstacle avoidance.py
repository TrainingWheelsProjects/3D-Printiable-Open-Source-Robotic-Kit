import time
from hcsr04 import HCSR04
import PicoRobotics

motorcontrol=PicoRobotics.KitronikPicoRobotics()
senseL=HCSR04(trigger_pin=15, echo_pin=4)
senseR=HCSR04(trigger_pin=13, echo_pin=12)
speedbase=25
speedchangeU=speedbase+10
speedchangeD=speedbase-10
while True:
    if senseL.distance>=20 and senseR.distance>=20:
        motorcontrol.motorOn(1,"r",speedbase)
        motorcontrol.motorOn(2,"r",speedbase)
    elif senseL.distance<20 and senseR.distance>=10:
        motorcontrol.motorOn(1,"r",speedchangeU)
        motorcontrol.motorOn(2,"r",speedchangeD)
    elif senseL.distance>=20 and senseR.distance<20:
        motorcontrol.motorOn(1,"r",speedchangeD)
        motorcontrol.motorOn(2,"r",speedchangeU)
    elif senseL.distance<20 and senseR.distance<20:
         motorcontrol.motorOff(1)
         motorcontrol.motorOff(2) 
    try:
        print((senseL.distance,"  " , senseR.distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.5)
        
motorcontrol.motorOff(1)
motorcontrol.motorOff(2)