from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time


def main():
    i2c = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=1_000_000)
    display = Display(i2c)

    while True:
        (year, month, mday, hour, minute, second, weekday, yearday) = time.localtime()
        hour = (hour-1)%12+1
        display.update(hour, minute, second)


class Display(SSD1306_I2C):
    def __init__(self, i2c):
        super().__init__(128, 64, i2c)
        
    def frame(self):
        "draw a decorative border"
        self.fill(0)
        self.rect(1, 1, 126, 62, 1)
        self.rect(5, 5, 118, 54, 1)
        self.rect(9, 9, 110, 46, 1)
        self.fill_rect(12, 12, 104, 40, 1)
        
    def update(self, hour, minute, second):
        self.frame()
        self.text("The time is", 20, 20, 0)
        self.text(f'{hour:2d}:{minute:02d}:{second:02d}', 35, 40, 0)
        self.show()


if __name__ == '__main__':
    main()