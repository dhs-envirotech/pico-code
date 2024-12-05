from machine import Pin
import utime
led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    print('on')
    utime.sleep_ms(1000)
    
    led.toggle()
    print('off')
    utime.sleep_ms(1000)
