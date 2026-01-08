# Create a program that "unlocks" a vault by requiring the user to input a code using one or two buttons.
# For example, you could use only a single button, and combination of long and short presses (eg SSLS).
# You could use two buttons (left and right), and the code could be (LLRL), ignoring the press duration.
# Or a combination of those for a more secure password! [3 marks]

# setup
from machine import Pin
import utime

# configuration
button_left = Pin(14, Pin.IN, Pin.PULL_UP)
button_right = Pin(27, Pin.IN, Pin.PULL_UP)
led_red = Pin(2, Pin.OUT)
led_green = Pin(4, Pin.OUT)

passcode = ['L', 'L', 'R', 'R']

current_input = []
last_action_time = utime.ticks_ms()

# run program
print("Vault Secured. Enter passcode.")
led_red.value(1) # Start locked

while True:
    # check left button
    if button_left.value() == 0:
        current_input.append('L')
        print("Input: Left")
        last_action_time = utime.ticks_ms()
        while button_left.value() == 0: # Wait for release (debounce)
            utime.sleep_ms(20)

    # check right button
    if button_right.value() == 0:
        current_input.append('R')
        print("Input: Right")
        last_action_time = utime.ticks_ms()
        while button_right.value() == 0: # Wait for release
            utime.sleep_ms(20)

    # check for inactivity
    if len(current_input) > 0:
        if utime.ticks_diff(utime.ticks_ms(), last_action_time) > 2000:
            print(f"Checking sequence: {current_input}")
            
            # check input
            if current_input == passcode:
                print("Vault Unlocked :)")
                led_red.value(0)
                led_green.value(1)
                utime.sleep(3)
                led_green.value(0)
                led_red.value(1)
            else:
                print("Incorrect Sequence :(")
                # flash red led
                for _ in range(5): # flash light 5 times
                    led_red.value(0); utime.sleep_ms(100)
                    led_red.value(1); utime.sleep_ms(100)
            
            current_input = [] # Reset for next attempt
            print("Enter code...")

    utime.sleep_ms(20) # small delay before loop starts back up

