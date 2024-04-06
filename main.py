pumpOnTime = 1
pumpOnPeriod = 5
lightOnTime = 1
lightOnPeriod = 10

import motor_control
import machine
import time
import _thread
pin25 = machine.Pin(25, machine.Pin.OUT)
pin16 = machine.Pin(16,machine.Pin.OUT)
adc = machine.ADC(machine.Pin(28))
lowLevel = 1000
level = adc.read_u16()
def lightOn() :
    pin25.high()
    return

def lightOff() :
    pin25.low()
    return

def pumpOnOff(timer,pumpOnTime) :
    if level < lowLevel :
        print("water level too low to run pump")
        return
    motor_control.motor_run_stop(True)
    time.sleep(pumpOnTime)
    motor_control.motor_run_stop(False) 
    return

timer =  machine.Timer()

pumpStartTime = time.ticks_ms()
lightStartTime = time.ticks_ms()
lightOn()

timer.init(mode = timer.PERIODIC, period = pumpOnPeriod*1000, callback = lambda t: pumpOnOff(t,pumpOnTime))
 
while True :
    level = adc.read_u16()
    if level < lowLevel :
        pin16.high()
    if level > lowLevel:
        pin16.low()
    while time.ticks_ms() - lightStartTime > lightOnTime *1000:
        lightOff()
        if time.ticks_ms() - lightStartTime > lightOnPeriod *1000 :  
            lightStartTime = time.ticks_ms()
            lightOn()
            break
        
            
            
        
        

