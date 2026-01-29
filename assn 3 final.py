# matthew pohl and willow woon chem 411 assignment 3
import machine as m
from machine import Pin, I2C
import time
import i2c_lcd
from hcsr04 import HCSR04

# setup
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
buzzer = Pin(19, Pin.OUT) # inverse buzzer (active, not passive)
screen = I2C(0, scl=Pin(22), sda=Pin(23))
lcd = i2c_lcd.I2cLcd(screen, 0x27, 2, 16)
button = Pin(14, Pin.IN, Pin.PULL_UP)

# functions!
def display():
    #display current distance
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str(round(distance,1)))
    lcd.move_to(5, 0)
    lcd.putstr('cm')
    
    #display max value
    lcd.move_to(0, 1)
    lcd.putstr('max')
    lcd.move_to(3,1)
    lcd.putstr(str(round(Max,1)))
    
    # display min value
    lcd.move_to(8, 1)
    lcd.putstr('min')
    lcd.move_to(12,1)
    lcd.putstr(str(round(Min,1)))

def handle_interrupt(pin): # button interrupt the while True loop modified from debouncing_03_professional.py
    global last_press_time, reset
    current_time = time.ticks_ms()
    
    # Check if enough time has passed since last valid press
    if time.ticks_diff(current_time, last_press_time) > debounce_interval:
        reset = True
        last_press_time = current_time

# Attach the interrupt to the pin
# Trigger on FALLING edge (when button goes from High to Low)
button.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

# variables
Min = None
Max = None
reset = False
count = 0
buzzer.value(1)
last_press_time = 0
debounce_interval = 500


while True:
    
    if reset: # for the reset button!
        Min = None
        Max = None
        reset = False
        buzzer.value(1)
        count = 0
        
    distance = sensor.distance_cm() # sensor takes a reading
    
    if Min == None and Max == None: # if starting from the beginning or if code has been reset
        Min = distance
        Max = distance

    if distance > Max: # check if the max value
        Max = distance
        
        for count in range (3):
            buzzer.value(0)
            time.sleep_ms(250)
            buzzer.value(1)
            time.sleep_ms(25)        

    elif distance < Min: # check if the min value
        Min = distance
        
        for count in range (3):
            buzzer.value(0)
            time.sleep_ms(150)
            buzzer.value(1)
            time.sleep_ms(25)

    display() # put all this info onto the lcd screen
    time.sleep_ms(1000) # check every 1s
