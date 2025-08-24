from machine import Pin

led = Pin(25, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_UP)
#            ^ change this number

print("Starting")
while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()