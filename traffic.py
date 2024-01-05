from enum import Enum
import RPi.GPIO as GPIO


class Light(Enum):
    ON = 0
    OFF = 1


class Signal:
    def __init__(self, pin: int, color: str, hex: str = '#dedede'):
        self.pin = pin
        self.col = color
        self.hex = hex
        self.setup_gpio()
                
    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        
    def set_light(self, light: Light):
        current: int = GPIO.input(self.pin)
        if current != light.value:
            GPIO.output(self.pin, light.value)
            
    def status(self):
        current = GPIO.input(self.pin)
        statstr = Light.OFF.name
        if current == Light.ON.value:
            statstr = Light.ON.name
        return {
            "pin": self.pin, 
            "color": self.col, 
            "hex": self.hex, 
            "status": statstr, 
            "value": current
        }
        