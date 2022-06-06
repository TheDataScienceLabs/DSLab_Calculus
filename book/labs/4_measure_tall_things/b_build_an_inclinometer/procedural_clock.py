from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time


i2c = I2C(id=1, sda=Pin(18), scl=Pin(19), freq=400_000)
screen = SSD1306_I2C(128, 64, i2c)

while True:
    (year, month, mday, hour, minute, second, weekday, yearday) = time.localtime()
    hour = (hour-1)%12+1
    
    # draw a decorative border
    screen.fill(0)
    screen.rect(1, 1, 126, 62, 1)
    screen.rect(5, 5, 118, 54, 1)
    screen.rect(9, 9, 110, 46, 1)
    screen.fill_rect(12, 12, 104, 40, 1)
    
    screen.text("The time is", 20, 20, 0)
    screen.text(f'{hour:2d}:{minute:02d}:{second:02d}', 35, 40, 0)
    screen.show()
