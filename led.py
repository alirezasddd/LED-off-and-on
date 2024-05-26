
from gpiozero import LED, Device
from gpiozero.pins.mock import MockFactory
from time import sleep

# تنظیم پین فکتوری به MockFactory
Device.pin_factory = MockFactory()

def blink_led(pin):
    led = LED(pin)
    try:
        while True:
            led.on()
            print("LED is on")
            sleep(5)
            led.off()
            print("LED is off")
            sleep(3)
    except KeyboardInterrupt:
        pass

blink_led(17)
