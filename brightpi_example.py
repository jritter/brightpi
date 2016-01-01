#!/usr/bin/python

from brightpi import *
import time

#switch_white_leds_on()

#for led in [2, 4, 5, 7]:
#    for i in range(0, 50):
#        dim_led(led, i)
#        time.sleep(0.1)
#
#    for i in range(-50, 0):
#        dim_led(led, abs(i))
#        time.sleep(0.1)

try:
    while True:
        for led in [2, 4, 5, 7]:
            dim_led(led, 50)
            switch_led_on(led)
            time.sleep(0.05)

except KeyboardInterrupt:
    switch_leds_off()
