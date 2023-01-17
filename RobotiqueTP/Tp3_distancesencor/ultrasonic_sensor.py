from hcsr04 import HCSR04
import time
from machine import Pin

sensor = HCSR04(trigger_pin=3, echo_pin=4)
led = Pin(28, Pin.OUT)



while 1:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep_ms(1)
    if distance < 70:
        led.value(1)
    else:
        led.value(0)
    