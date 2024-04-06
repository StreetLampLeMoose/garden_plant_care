import machine
motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)
def motor_run_stop(run_state) :
    if run_state == True:
            motor1A.high()
            motor2A.low()
            return print("motor running")     
    if run_state == False:
            motor1A.low()
            motor2A.low()
            return print("motor stopped")
