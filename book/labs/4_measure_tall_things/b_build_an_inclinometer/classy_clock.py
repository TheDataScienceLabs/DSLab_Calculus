from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time


def main():
    i2c = I2C(id=1, sda=Pin(18), scl=Pin(19), freq=3_400_000)
    display = Display(i2c)

    while True:
        (year, month, mday, hour, minute, second, weekday, yearday) = time.localtime()
        hour = (hour-1)%12+1
        display.update(hour, minute, second)


class Display:
    def __init__(self, i2c):
        self.screen = SSD1306_I2C(128, 64, i2c)
        
    def frame(self):
        "draw a decorative border"
        self.screen.fill(0)
        self.screen.rect(1, 1, 126, 62, 1)
        self.screen.rect(5, 5, 118, 54, 1)
        self.screen.rect(9, 9, 110, 46, 1)
        self.screen.fill_rect(12, 12, 104, 40, 1)
        
    def update(self, hour, minute, second):
        self.frame()
        self.screen.text("The time is", 20, 20, 0)
        self.screen.text(f'{hour:2d}:{minute:02d}:{second:02d}', 35, 40, 0)
        self.screen.show()


if __name__ == '__main__':
    main()