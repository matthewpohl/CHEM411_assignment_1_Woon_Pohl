from machine import Pin, I2C, ADC
import time, i2c_lcd

button_left = Pin(14, Pin.IN, Pin.PULL_UP)
button_right = Pin(12, Pin.IN, Pin.PULL_UP)
lcd_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(lcd_device, 0x27, 2, 16)


passcode = 'LLRR' # define passcode as a list 

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
            print('left')
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(str(current_input)) # print the list of inputs e.g., LLRL
            time.sleep_ms(200)
            
        # check if the RIGHT button is pressed
        if button_right.value() == 0:
            current_input += 'R' # append 'R' to the list
            last_input_time == time.ticks_ms()
            print('right')
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(str(current_input)) # print the list of inputs e.g., LRR
            time.sleep_ms(200)

        if len(current_input) == len(passcode):
            if time.ticks_diff(time.ticks_ms(), last_input_time) > 2000 or len(current_input) >= len(passcode):
                if current_input == passcode:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr('access granted')
                    lcd.move_to(0,1)
                    lcd.putstr('correct passcode')
                    time.sleep_ms(100)

                else:
                    lcd.clear()
                    lcd.move_to(0,0)
                    lcd.putstr('access denied')
                    lcd.move_to(0,1)
                    lcd.putstr('wrong passcode')
                    time.sleep_ms(100)
                current_input = ''
                time.sleep_ms(2000)
                lcd.move_to(0,0)
                lcd.clear()
                lcd.putstr('ready 4 input')
                

