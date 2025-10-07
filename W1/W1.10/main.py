import dht
from machine import Pin
from time import sleep

sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"Temperature: {temp:.1f}°C, Humidity: {hum:.1f}%")
    sleep(2)
