# setup
from machine import Pin, ADC, I2C
import i2c_lcd, time 

# configure
i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)
led = Pin(14, Pin.OUT)
dark_level = 1000
lcd.clear()

while True:
    
    lcd.move_to(0, 0) # center text on first line of LCD
    lcd.putstr("light: %d" %ldr.read() ) # display light level
    time.sleep_ms(100)
    
        
    if ldr.read() > dark_level: # if value of ldr.read() is under dark_level, turn on
        led.value(1)
        lcd.move_to(0, 1) # center text on second line of LCD
        lcd.putstr("light on!" ) # display 'light on!'
        time.sleep_ms(50)
        
    else: # else turn off
        led.value(0)
        lcd.move_to(0, 1) # center text on second line of LCD
        lcd.putstr("light off :(" ) # display 'light off :('

        
