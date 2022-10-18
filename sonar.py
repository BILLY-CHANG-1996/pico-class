import time
from machine import Pin, PWM
from time import sleep
import HC_SR04
pwm = PWM(Pin(16))
pin_led = machine.Pin(25, machine.Pin.OUT)
pwm.duty_u16(10000)
duration = 0
trig = Pin(10,Pin.OUT)
echo = Pin(4,Pin.IN)

def ping():
    global duration
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count = 0
    timeout = False
    start = time.ticks_us()
    while not echo.value(): #wait for high
        time.sleep_us(10)
        cout += 1
        if count > 100000: #over 1s timeout
            timeout = True
            break
        if timeout:#timeout return 0
            duration = 0
        else:
            count = 0
            start = time.ticks_us()
            while echo.value():
                time.sleep_us(10)
                count += 1
                if count > 2320:
                    break
            duration = time.ticks_diff(time.ticks_us(),start)
        return duration
    
while True:
    distance = round(ping()/58)
    if distance < 15:
        for duty in range(600,5000,200):
            pwm.freq(432)
            sleep(1)
            print("123")
            print("%scm"% distance)
            time.sleep(0.5)
                           