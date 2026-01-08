# Write some micropython code that can register and report short vs long presses of the button.
# You can decide the threshold between a short and long press
# (example, short is less than 0.5 s, long is greater than 1 s). [2 marks]

# setup
from machine import Pin
import utime

# configuration
button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(12, Pin.OUT)

# thresholds in milliseconds
short = 500
long = 1000

print("System Ready. Press the button!")

while True:
    # wait for press (0 is on because of PULL_UP)
    if button.value() == 0:
        stime = utime.ticks_ms() # start time
        
        # wait for release
        while button.value() == 0:
            utime.sleep_ms(10) # Debounce/Efficiency
        
        etime = utime.ticks_ms() # end time
        
        # calculate duration
        eltime = utime.ticks_diff(etime, stime) # elapsed time
        
        # report results
        if eltime >= long:
            print(f"Long Press Detected! ({eltime}ms)")
            led.value(1)
            utime.sleep(2)
            led.value(0)
            utime.sleep(0.1)
        elif eltime <= short:
            print(f"Short Press Detected! ({eltime}ms)")
            led.value(1)
            utime.sleep(0.5)
            led.value(0)
            utime.sleep(0.1)
        else:
            print(f"Medium Press ({eltime}ms)")
            led.value(1)
            utime.sleep(1)
            led.value(0)
            utime.sleep(0.1)
            
            
    utime.sleep_ms(20) # small delay before loop starts back up