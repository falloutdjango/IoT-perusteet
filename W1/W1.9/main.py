from machine import Pin
from time import sleep

pir = Pin(14, Pin.IN)
led = Pin(15, Pin.OUT)
buzzer = Pin(16, Pin.OUT)

while True:
    if pir.value() == 1:
        print("Motion detected!")
        led.on()
        buzzer.on()
        sleep(2)
        led.off()
        buzzer.off()
    sleep(0.1)
