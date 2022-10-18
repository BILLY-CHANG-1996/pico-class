from machine import Pin, PWM
from time import sleep


pwm = PWM(Pin(16))
pin_led = machine.Pin(25, machine.Pin.OUT)
pwm.duty_u16(10000)

while True:
    for duty in range(600,5000,200):
        pwm.freq(432)
        sleep(1)
        pwm.freq(415)
        sleep(1)
        pwm.freq(392)
        sleep(1)
        pwm.freq(369)
        sleep(1)
        pwm.freq(349)
        sleep(1)
        pwm.freq(329)
        sleep(1)
        pwm.freq(311)
        sleep(1)
        pwm.freq(293)
        sleep(1)