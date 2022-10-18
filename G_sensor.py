from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda = Pin(12), scl = Pin(13), freq = 100000)
i2c.start
i2c.writeto(0x19, bytes([0x20, 0x47]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x21, 0x80]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x22, 0x00]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x23, 0x00]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x24, 0x40]))
i2c.stop
i2c.start
i2c.writeto(0x19, bytes([0x25, 0x00]))
i2c.stop
i2c.start

while True:
    i2c.start
    i2c.writeto(0x19, bytes([0xa8]))
    data = i2c.readfrom(0x19,6)
    x= round((((data[0])>>6|(data[1])<<2)/2.8),1)
    y= round((((data[2])>>6|(data[3])<<2)/2.8),1)
    z= round((((data[4])>>6|(data[5])<<2)/2.8),1)
    print('{}{:5}{}{:5}{}{:5}'.format("X =",x,"Y =",y,"Z =",z))
    sleep(0.5)
