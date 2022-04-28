# Write your code here :-)
import rotaryio
import board
import PicoRobotics
import math
motorcontrol=PicoRobotics.KitronikPicoRobotics()
encoder1= rotaryio.IncrementalEncoder(board.GP1, board.GP0)
encoder2= rotaryio.IncrementalEncoder(board.GP2, board.GP3)
wheelR=13.75/1000
tickL=encoder1.position
tickR=encoder2.position
tickspR=960
while True:
    tickL=encoder1.position
    tickR=encoder2.position
    motorcontrol.motorOn(2,"r",20)
    motorcontrol.motorOn(1,"r",20)
        
    travelL=((2*math.pi*wheelR)/tickspR)*tickL
    travelR=((2*math.pi*wheelR)/tickspR)*tickR
    dist=(travelL+travelR)/2
    print(dist)
    if dist>=1:
        motorcontrol.motorOff(1)
        motorcontrol.motorOff(2)
        break
    
        
