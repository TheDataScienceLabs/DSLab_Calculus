# Imports
import time
import math
from machine import Pin, I2C
from imu import MPU6050
from ssd1306 import SSD1306_I2C
from averager import Averager


def main():
    i2c = I2C(id=____, sda=Pin(_____), scl=Pin(____), freq=400_000) # Fill In Based on Pin Sheet
    led = Pin(25, Pin.OUT)
    button = Pin(____, Pin.IN, Pin.PULL_UP) # Fill In Based on Pin Sheet
    inclinometer = Inclinometer(i2c, button, led)
    while True:
        inclinometer.write()
        for i in range(50):
            inclinometer.read()
        
    
class Inclinometer:
    def __init__(self, i2c, button, led, samples = 50):
        self.display = Display(i2c)
        self.accelerometer = MPU6050(i2c)
        self.button = button
        self.led = led
        # Define x, y, and z as Averager Objects(Look at Parameters For Sample Size!)
        self.x = ____
        self.y = ____
        self.z = ____
        
    def read(self):
        x, y, z = self.accelerometer.accel.x, self.accelerometer.accel.y, self.accelerometer.accel.z
        # Add x, y, and z values into Averager Object 
        ____ # x
        ____ # y
        ____ # z
        
    def write(self):
        if self.button.value():
            # Get x, y, and z values from Average Object
            x = ____
            y = ____
            z = ____
            self.display.update(x, y, z)
        else:
            self.display.hold()
        

class Display(SSD1306_I2C):
    def __init__(self, i2c):
        super().__init__(128, 64, i2c)
        self.fill(0)
        self.text('loading...', 0, 0, 1)
        self.show()
        
    def update(self, x, y, z):
        # Print Out x, y, and z values
        self.fill(0)
        self.text(____, 0, 10, 1)
        self.text(____, 0, 20, 1)
        self.text(____, 0, 30, 1)
        self.text("-", 0, 40, 1)
        self.show()
        
    def hold(self):
        self.fill_rect(0, 0, 32, 9, 1)
        self.text("HOLD", 0, 1, 0)
        self.show()
        
        
if __name__ == '__main__':
    main()
