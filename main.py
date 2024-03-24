import motor_run_stop
adc = machine.ADC(machine.Pin(28))

while True:
    level = adc.read_u16()
    while level > 1000:
        
        motor_run_stop.motor_run_stop(True)
    while level < 1000 :
        
        motor_run_stop.motor_run_stop(False)
        