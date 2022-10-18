import machine
import time
from machine import Pin, PWM
from time import sleep

x=machine.ADC(26)
y=machine.ADC(28)
servoPin_X = PWM(Pin(16))
servoPin_X.freq(50)
servoPin_Y = PWM(Pin(17))
servoPin_Y.freq(50)

time.sleep(0.001)
x_zero = x.read_u16()/100
y_zero = y.read_u16()/100

def servo(degrees,degrees1):
    maxDuty = 9000 
    minDuty = 1000
    newDuty_x = minDuty + (maxDuty - minDuty)*(degrees/180)
    newDuty_y = minDuty + (maxDuty - minDuty)*(degrees1/180)
    servoPin_X.duty_u16(int(newDuty_x))
    servoPin_Y.duty_u16(int(newDuty_y))

def joystick():
    reading=x.read_u16()
    x_data = round(x_zero-reading/100)
    print('X= ',x_data)
    reading=y.read_u16()
    y_data = round(y_zero-reading/100)
    print('Y= ',y_data)
    time.sleep(0.001)
    return (x_data, y_data)
    
while True:
    a,b = joystick()
    servo((a/4)+90, (b/4)+90)
    sleep(0.001)
        
    
    

        

    
    