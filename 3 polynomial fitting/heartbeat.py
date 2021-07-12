import machine
from time import sleep

heart = machine.ADC(26)

while True:
    print(heart.read_u16())
    sleep(1/200)