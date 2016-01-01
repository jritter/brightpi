#!/usr/bin/python
#
# Library controls the leds on the bright pi circuit
# https://www.pi-supply.com/product/bright-pi-bright-white-ir-camera-light-raspberry-pi/
# 
# this circuit uses the Semtech SC620 LED driver chip
# Datasheet: http://www.semtech.com/images/datasheet/sc620.pdf
# 
# Additional documentation: https://www.pi-supply.com/bright-pi-v1-0-code-examples/
#
# White LEDs:
#   2, 4, 5, 7
# IR LEDs (in pairs)
#   1, 3, 6, 8
#

import smbus

bus = smbus.SMBus(1)


DEVICE_ADDRESS        = 0x70
LED_CONTROL_ALL_WHITE = 0x5a
LED_CONTROL_ALL_IR    = 0xa5
LED_GAIN_REGISTER     = 0x09



def switch_white_leds_on():
    bus.write_byte_data(DEVICE_ADDRESS, 0x00, LED_CONTROL_ALL_WHITE)

def switch_ir_leds_on():
    bus.write_byte_data(DEVICE_ADDRESS, 0x00, LED_CONTROL_ALL_IR)

def switch_leds_off():
    bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0x00)

def switch_led_on(led):
    if led >= 1 and led <= 8:
        bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0b1 << led - 1)

def set_gain(gain):
    # gain is a 4 bit value
    if gain >= 0 and gain <= 15:
        bus.write_byte_data(DEVICE_ADDRESS, LED_GAIN_REGISTER, gain)
    
def set_default_gain():
    # default gain is 0b1000
    bus.write_byte_data(DEVICE_ADDRESS, LED_GAIN_REGISTER, 0b1000)

def dim_led(led, value):
    # there are 8 LEDs (1-8) and
    # dim values range between 0 and 50
    if led >= 1 and led <= 8 and value >= 0 and value <= 50:
        bus.write_byte_data(DEVICE_ADDRESS, led, value)
