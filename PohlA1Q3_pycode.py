# Make a nightlight that turns on automatically when it gets dark, as determined by a light sensor.
# You can determine what threshold intensity value you wish to use. [2 marks]

# setup
from machine import ADC, Pin
import utime

# configure ADC on GPIO 34 (pin D34, analog signal input)
ldr = ADC(Pin(34))
led = Pin(12, Pin.OUT)

# configure attenuation for full 0-3.3V range, allowing the ESP32 to read the full range of the sensor
ldr.atten(ADC.ATTN_11DB)
dark_level = 1800

while True:
    if ldr.read() > dark_level:
        led.value(1)
    else:
        led.value(0)
            
utime.sleep_ms(20) # small delay before loop starts back up

      