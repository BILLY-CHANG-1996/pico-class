from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
from time import sleep
import time
sensor_vol = machine.ADC(1)
conversion_factor = 3.3/65535

comm = machine.UART(1,115200)
#comm.init(9600, bits = 8, parity = None, stop = 1, time out = 2000)
uart = UART(0, tx = Pin(0), rx = Pin(1))
#iniit Display
i2c = I2C(0, sda = Pin(12), scl = Pin(13), freq = 40000)
oled = SSD1306_I2C(128, 32, i2c)
oled.fill(0)

while True:
    vol = sensor_vol.read_u16()*conversion_factor

    vol_a = round(vol,2)
    vol_b = round(vol)
    isp = float(vol_a)
    print(isp)
    sleep(0.02)
    
    for i in range(0, 2, 1):
        disp = str(i)
        oled.text(disp, 10 , 12)
        oled.show()
        time.sleep(0.5)
        oled.fill(0)
        isp = str(isp)
        oled.text(isp, 10,12)
        oled.show()
