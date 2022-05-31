from machine import Pin

led = Pin(25, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()