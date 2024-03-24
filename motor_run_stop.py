import machine
import utime
import time
motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)
adc = machine.ADC(machine.Pin(28))
def motor_run_stop(run_state) :
    while run_state == True:
            time.sleep(0.25)
            motor1A.high()
            motor2A.low()
            if adc.read_u16() < 1000 :
                return 0
                
    while run_state == False:
            time.sleep(0.25)
            motor1A.low()
            motor2A.low()
            if adc.read_u16() > 1000 :
                return 0