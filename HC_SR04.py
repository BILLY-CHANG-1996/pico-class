import time,math
from machine import Pin
from time import sleep
from machine import Pin, PWM
#import usonic

pin_led = Pin(25, Pin.OUT)
trig = Pin(10, Pin.OUT)
echo = Pin(4, Pin.IN,Pin.PULL_DOWN)
pwm = PWM(Pin(16))
pin_led = machine.Pin(25, machine.Pin.OUT)
pwm.duty_u16(10000)
trig = Pin(10,Pin.OUT)
echo = Pin(4,Pin.IN)

def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=0
    timeout=False
    start=time.ticks_us()
    while not echo.value(): #wait for HIGH
        time.sleep_us(10)
        count += 1
        if count > 10000: #over 1s timeout
            timeout=True
            break
    if timeout: #timeout return 0
        duration=0
    else: #got HIGH pulse:calculate duration
        count=0
        start=time.ticks_us()
        while echo.value(): #wait for LOW
            time.sleep_us(10)
            count += 1
            if count > 2320: #over 400cm range:quit
                break
        duration=time.ticks_diff(time.ticks_us(), start)
    return duration   
def bi():
    for i in range (3000):
        pwm.value(1)
        time.sleep_us(150)
        pwm.value(0)
        time.sleep_us(150)
        
while True:
    distance=round(ping()/58)
    print("%scm" % distance)
    if distance < 15 :
        pin_led.on()
        bi()
        time.sleep(1)
        
    else :
        pin_led.off()
        time.sleep(0.5)