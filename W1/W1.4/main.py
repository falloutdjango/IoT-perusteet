# blink_optimized.py
from machine import Pin
from time import sleep

def blink(pin, delay):
    led = Pin(pin, Pin.OUT)
    while True:
        led.toggle()
        sleep(delay)

blink('LED', 0.2)
