# setup
from machine import Pin, I2C, ADC
import time, i2c_lcd

# configure
button_left = Pin(14, Pin.IN, Pin.PULL_UP)
button_right = Pin(12, Pin.IN, Pin.PULL_UP)
lcd_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(lcd_device, 0x27, 2, 16)


passcode = 'LLRR' # define passcode as a list # define passcode solution

current_input = ''
last_input_time = time.ticks_ms()

lcd.move_to(0,0)
lcd.clear()
lcd.putstr('ready 4 input')

while True:
    
        # check if the LEFT button is pressed
        if button_left.value() == 0:
            current_input += 'L' # append 'L' to the list
            last_input_time == time.ticks_ms()
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(str(current_input)) # print the list of inputs e.g., LLRL
            time.sleep_ms(200)
            
        # check if the RIGHT button is pressed
        if button_right.value() == 0:
            current_input += 'R' # append 'R' to the list
            last_input_time == time.ticks_ms()
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(str(current_input)) # print the list of inputs e.g., LRR
            time.sleep_ms(200)

        # if the passcode is 4 characters long, check if it matches the 'passcode' and display whether or not it is correct on the LCD
        if len(current_input) == len(passcode):
            if current_input == passcode:
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr('access granted') # display 'access granted' on the LCD
                lcd.move_to(0,1) # move to the next line
                lcd.putstr('correct passcode') # display 'correct passcode' on the LCD
                time.sleep_ms(100)

            else:
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr('access denied') # display 'access denied' on the LCD
                lcd.move_to(0,1) # move to next line
                lcd.putstr('wrong passcode') # display 'wrong passcode' on the LCD
                time.sleep_ms(100)

            # reset for next input
            current_input = ''
            time.sleep_ms(2000)
            lcd.move_to(0,0)
            lcd.clear()
            lcd.putstr('ready 4 input')
                


