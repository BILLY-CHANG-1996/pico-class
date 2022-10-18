import machine
from time import sleep
from machine import Pin,PWM
pin_led25 = machine.Pin(25,machine.Pin.OUT)
pin_led14 = machine.Pin(14,machine.Pin.OUT)
pin_led15 = machine.Pin(15,machine.Pin.OUT)
buzz = PWM(Pin(16))
while True:
    pin_led25.on()
    sleep(0.1)
    pin_led25.off()
    sleep(0.1)
    pin_led14.on()
    sleep(0.1)
    pin_led14.off()
    sleep(0.1)
    pin_led15.on()
    sleep(0.1)
    pin_led15.off()
    sleep(0.1)
    pin_led14.on()
    sleep(0.1)
    pin_led14.off()
    sleep(0.1)