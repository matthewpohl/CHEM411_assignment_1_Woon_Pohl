# setup things you are gonna need. 
from machine import Pin, ADC, I2C
import i2c_lcd, time 

# setup
#potentiometer = ADC(Pin(34))
#potentiometer.ATTN_11DB   # know in advance you're gonna supply 3.3V, so:
i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)   # don't need to do the device print thingy
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)
led = Pin(14, Pin.OUT)
# connect vout of potentiometer to pin 32
# vcc to input voltage (put 3.3V)
# connect AO or DO
# he put AO on Pin34

lcd.clear()
while True:   # a loop that goes on forever
    
   
    lcd.move_to(0, 0) #center text
    lcd.putstr("light: %d" %ldr.read() )
    time.sleep_ms(100)
    
        
    if ldr.read() > 1000:  # light is certain threshhold, turn on!
        led.value(1)
        lcd.move_to(0, 1) #center text
        lcd.putstr("light on!" )
        time.sleep(0.05)
        
    else:  #else turn off
        led.value(0)
        lcd.move_to(0, 1) #center text
        lcd.putstr("light off" )
        