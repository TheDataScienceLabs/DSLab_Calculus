import time
from machine import Pin, time_pulse_us

# these pins can be whatever -- just make sure
# the wires correspond with the correct GP pin number!
trig = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
# this refers to the built in LED. Just to give some
# visual indication of what is happening.
led = Pin(25, Pin.OUT)

trig.off()
led.off()
start = time.ticks_ms()

while True:
    # There has to be at least 60ms between measurements,
    # for the sensor to reset itself.
    time.sleep_ms(100)
    led.on()
    
    # A 10 ms pulse tells the sensor to begin a measurement.
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    # This built in function measures how long a pulse is.
    pulse = time_pulse_us(echo, 1, 1_000_000)
    
    now = time.ticks_ms() - start
    print(now, pulse)
    led.off()
