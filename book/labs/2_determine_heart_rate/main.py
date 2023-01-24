import machine
from time import sleep

heart = machine.ADC(26)

while True:
    rate, samples = input().split(',')
    period = 1/int(rate)
    for sample in range(int(samples)):
        print(heart.read_u16())
        sleep(period)
    print('done')