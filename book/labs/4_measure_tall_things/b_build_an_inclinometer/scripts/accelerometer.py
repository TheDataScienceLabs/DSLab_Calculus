from machine import Pin, I2C
from imu import MPU6050
import time

i2c = I2C(id=1, sda=Pin(18), scl=Pin(19), freq=400_000)
imu = MPU6050(i2c)

print("Starting")
while True:
    x = imu.accel.x
    y = imu.accel.y
    z = imu.accel.z
    print(f'x:{x: .4f}\ty:{y: .4f}\tz:{z: .4f}', end='\r')
    time.sleep(0.01)
