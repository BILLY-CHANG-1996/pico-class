import machine
from time import sleep


button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
pin_led = machine.Pin(25, machine.Pin.OUT)
x = 0


while True:
    if button.value() == 1:
        
        for i in range(x):
             x=5
        pin_led.on()
        sleep(0.5)
        pin_led.off()
        sleep(0.5)
    else:
        pin_led.off()
        
   