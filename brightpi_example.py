#!/usr/bin/python

from brightpi import *
import time

WHITE_LEDS = [2, 4, 5, 7]

try:
    for i in range(1, 5):
        for led in WHITE_LEDS:
            dim_led(led, 50)
            set_led_state(led, not get_led_state(led))
            time.sleep(0.1)

    # dim in LEDs
    for i in range(1, 30):
        for led in WHITE_LEDS:
            dim_led(led, i)
            set_led_state(led, True)
            time.sleep(0.05)

    # dim out LEDs
    for i in range(-30, -1):
        for led in WHITE_LEDS:
            dim_led(led, abs(i))
            set_led_state(led, True)
            time.sleep(0.05)

    switch_leds_off()

except KeyboardInterrupt:
    switch_leds_off()
