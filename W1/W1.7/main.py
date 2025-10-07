from machine import Pin
from time import sleep

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)
buzzer = Pin(12, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)

def normal_cycle_step():
    green.on()
    for _ in range(20):
        if button.value() == 0:
            return False
        sleep(0.1)
    green.off()

    yellow.on()
    for _ in range(10):
        if button.value() == 0:
            return False
        sleep(0.1)
    yellow.off()

    red.on()
    for _ in range(20):
        if button.value() == 0:
            return False
        sleep(0.1)
    red.off()

    return True

def alert_mode():
    red.on()
    buzzer.on()
    sleep(1)
    buzzer.off()
    red.off()

while True:
    if button.value() == 0:
        alert_mode()
    else:
        if not normal_cycle_step():
            alert_mode()
