# main.py for MAX30102
# reference code:
# https://github.com/n-elia/MAX30102-MicroPython-driver.git

from machine import SoftI2C, Pin
from time import sleep
from utime import ticks_diff, ticks_us

from max30102 import MAX30102
from max30102 import MAX30105_PULSE_AMP_LOWEST, MAX30105_PULSE_AMP_LOW, MAX30105_PULSE_AMP_MEDIUM, MAX30105_PULSE_AMP_HIGH


def main():
    my_SDA_pin = 0  # I2C SDA pin number
    my_SCL_pin = 1  # I2C SCL pin number
    my_i2c_freq = 400_000  # I2C frequency. Fast: 400KHz, slow: 100KHz
    
    # I2C instance
    i2c = SoftI2C(sda=Pin(my_SDA_pin),
                  scl=Pin(my_SCL_pin),
                  freq=my_i2c_freq)

    # Sensor instance
    sensor = MAX30102(i2c=i2c)  # An I2C instance is required

    # Scan I2C bus to ensure that the sensor is connected
    if sensor.i2c_address not in i2c.scan():
        print("Sensor not found.")
        return
    elif not (sensor.check_part_id()):
        # Check that the targeted sensor is compatible
        print("I2C device ID not corresponding to MAX30102 or MAX30105.")
        return
    else:
        print("Sensor connected and recognized.")

    # It's possible to set up the sensor at once with the setup_sensor() method.
    # If no parameters are supplied, the default config is loaded:
    # Led mode: 2 (RED + IR)
    # ADC range: 16384
    # Sample rate: 400 Hz
    # Led power: maximum (50.0mA - Presence detection of ~12 inch)
    # Averaged samples: 8
    # pulse width: 411
    
    # Setup with default values
    print("Setting up sensor with default configuration.", '\n')
    sensor.setup_sensor()

    # We can tune the configuration parameters one by one.
    
    # # 1. Set the sample rate
    # SAMPLE_RATE = 200 # Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
    # sensor.set_sample_rate(SAMPLE_RATE)
    # # 2. Set the number of samples to be averaged per each reading
    # SAMPLE_AVG = 1 # Options: 1, 2, 4, 8, 16, 32
    # sensor.set_fifo_average(SAMPLE_AVG)
    # # 3. Set the ADC range
    # ADC_RANGE = 16384  # Options: 2048, 4096, 8192, 16384
    # sensor.set_adc_range(ADC_RANGE)
    # # 4. Set the Pulse Width
    # PULSE_WIDTH = 411  # Options: 69, 118, 215, 411
    # sensor.set_pulse_width(PULSE_WIDTH)
    # # 5. Set the LED mode
    # LED_MODE = 1  # Options: 1 (red), 2 (red + IR)
    # sensor.set_led_mode(LED_MODE)
    # # 6. Set the LED brightness of each LED
    # LED_POWER = MAX30105_PULSE_AMP_MEDIUM
    # Options:
    # # MAX30105_PULSE_AMP_LOWEST =  0x02 # 0.4mA  - Presence detection of ~4 inch
    # # MAX30105_PULSE_AMP_LOW =     0x1F # 6.4mA  - Presence detection of ~8 inch
    # # MAX30105_PULSE_AMP_MEDIUM =  0x7F # 25.4mA - Presence detection of ~8 inch
    # # MAX30105_PULSE_AMP_HIGH =    0xFF # 50.0mA - Presence detection of ~12 inch
    # sensor.set_pulse_amplitude_red(LED_POWER)
    # sensor.set_pulse_amplitude_it(LED_POWER)    
    
    # Set the LED mode
    LED_MODE = 1
    sensor.set_led_mode(LED_MODE)
    
    # Set the LED brightness of each LED
    LED_POWER = MAX30105_PULSE_AMP_MEDIUM
    sensor.set_pulse_amplitude_red(LED_POWER)
    sensor.set_pulse_amplitude_it(LED_POWER)
    
    # Set the number of samples to be averaged per each reading
    SAMPLE_AVG = 1
    sensor.set_fifo_average(SAMPLE_AVG)
    
    # Set the sample rate
    SAMPLE_RATE = 64 #int(input('SAMPLE_RATE = ')) # Set the variable value by the user.
    sensor.set_sample_rate(SAMPLE_RATE)
    
    print("Starting data acquisition...")
    
    sleep(0.5)
    
    while True:                    
        # The check() method has to be continuously polled, to check if
        # there are new readings into the sensor's FIFO queue. When new
        # readings are available, this function will put them into the storage.
        sensor.check()

        # Check if the storage contains available samples
        # *Note: Some sensors have the red and IR registers inverted (or maybe the LEDs swapped)!
        # You can easily check if your sensor is inverted by putting it in LED mode 1: only the red LED should work.
        # If you see the IR LED (use your phone camera to check), then you have to collect IR samples as red ones and viceversa.
        if sensor.available():            
            # Access the storage FIFO and gather the readings (integers)
            red_reading = sensor.pop_red_from_storage()
            ir_reading = sensor.pop_ir_from_storage()

            # Print the acquired data (so that it can be plotted with a Serial Plotter)
            print(-red_reading+50000) # it is IR in the sensor purchased, it can be different in other sensor
                



if __name__ == '__main__':
    main()

