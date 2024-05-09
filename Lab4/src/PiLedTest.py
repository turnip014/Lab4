import time as t
from hal import hal_input_switch as his
from hal import hal_led as led
from hal import hal_buzzer as buzz

def switch_init():
    value = his.read_slide_switch()
    if value == 1:
        led.set_output(0,0)
        buzz.turn_off()
    elif value == 0:
        led.set_output(0,1)
        buzz.turn_on()
        t.sleep(0.05)
        led.set_output(0,0)
        buzz.turn_off()
        t.sleep(0.05)
    return

buzz.init()
his.init()
led.init()

while(1):
    switch_init()
