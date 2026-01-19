# matthew pohl and willow woon
# setup
from machine import Pin, I2C
import i2c_lcd, time

# configure
button = Pin(12, Pin.IN, Pin.PULL_UP)
screen = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(screen, 0x27, 2, 16)

press_start = None

while True:
    if button.value() == 0 and press_start is None: # button pressed and prevent bounce/recording several start times
        press_start = time.ticks_ms() # assign start_time as the time when the button is initially pressed
        
    elif button.value() == 1 and press_start is not None: # press_start is not blank
        press_end = time.ticks_ms() # assign press_end as the time when the button is released
        duration = time.ticks_diff(press_end, press_start) # time that button was released - time it was started in ms
        press_start = None # clears start time so button can be pressed again
        
        # if the button is pressed for a short time (0 ms < t < 500 ms)
        if duration < 500:
            lcd.clear()
            lcd.move_to(2, 0) # center text
            lcd.putstr('short press') # display 'short press'
            lcd.move_to(5, 1) # center text
            lcd.putstr(str(duration)) # print the duration of the press
            lcd.move_to(9,1)
            lcd.putstr('ms') # display units of time
            time.sleep(0.3)
            
        # if the button is pressed for a long time (500 ms < t < 2000 ms)
        elif duration >= 500 and duration <= 2000:
            lcd.clear()
            lcd.move_to(3, 0) # center text
            lcd.putstr('long press') # display 'long press'
            lcd.move_to(5, 1)
            lcd.putstr(str(duration)) # print the duration of the press
            lcd.move_to(9,1)
            lcd.putstr('ms') # display units of time
            time.sleep(0.3)
            
        # if the button is pressed for too long (t > 2000 ms)
        # *self-destruct sequence
        elif duration > 2000:
            lcd.clear()
            lcd.move_to(1, 0) # center the text
            lcd.putstr('press too long') # display 'press too long'
            lcd.move_to(1, 1) # move to second line, and center text
            lcd.putstr('self destruct') # display 'self destruct'
            time.sleep(2)
            lcd.clear()
            count = 3

            # count down to 0 from 3
            while count >= 0:
                lcd.move_to(7, 1) 
                lcd.putstr(str(count))
                count -= 1
                time.sleep(1)

            # after 0, display 'boom!' on the LCD
            else:
                lcd.clear()
                lcd.move_to(6, 0)
                lcd.putstr('boom!')
                time.sleep(0.3)

    time.sleep_ms(10) # let the microprocessor rest momentarily

