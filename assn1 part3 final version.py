# matthew pohl and willow woon

# setup things you are gonna need. 
from machine import Pin, ADC, I2C
import i2c_lcd, time 

# setup

i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)
led = Pin(14, Pin.OUT)
# vcc to input voltage (put 3.3V)
# connect AO or DO
# he put AO on Pin34

lcd.clear()
while True:   # a loop that goes on forever
    
    lcd.move_to(7, 0) 
    lcd.putstr("     ") #clears prev value so 2 or 3 digit values can be displayed without previous 4 digit showing
    lcd.move_to(0, 0)
    lcd.putstr("light: %d" %ldr.read() )
    print(ldr.read())
    time.sleep_ms(100)
    
        
    if ldr.read() < 2500:  # light is certain threshhold, turn off
        led.value(0)
        lcd.move_to(0, 1) 
        lcd.putstr("light off")
        time.sleep(0.50)
        
    else:  #else turn on
        led.value(1)
        lcd.move_to(0, 1) 
        lcd.putstr("light on!" ) # use ! so that it covers the last 'f' of 'light off' w/o a clear
        time.sleep(0.50)
        