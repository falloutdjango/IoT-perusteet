from machine import Pin
from time import sleep, ticks_ms, ticks_diff
import urandom

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

print("Get ready...")

while True:
    sleep(urandom.uniform(2, 5))  # satunnainen odotus
    led.on()
    start = ticks_ms()

    # odotetaan napin painallusta
    while button.value() == 1:
        pass

    reaction = ticks_diff(ticks_ms(), start)
    led.off()
    print("Reaction time:", reaction, "ms")
    sleep(2)
