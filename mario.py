from machine import Pin,PWM
import time

def mario(pwm):
    pwm.freq(659) #E5        
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep_ms(150)
    pwm.freq(659) #E5
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep_ms(150)
    pwm.freq(659) #E5
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep_ms(150)
    time.sleep_ms(150)
    pwm.freq(523) #C5
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep_ms(150)
    pwm.freq(659) #E5
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep_ms(150)
    time.sleep_ms(150)
    pwm.freq(784) #G5
    pwm.duty_u16(512)
    time.sleep_ms(150)
    pwm.deinit()
    time.sleep(3)

pwm=PWM(Pin(16))

while True:
    for duty in range(600,5000,200):
        mario(pwm)