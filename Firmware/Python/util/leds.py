from pwmio import PWMOut
from util.constants import LED_INTENSITY, LED_PINS


class Leds:
    def __init__(self):
        self.profiles = {}
        self.leds = []
        self.intensity = LED_INTENSITY

        self.setup_leds()

    def setup_leds(self):
        for pin in LED_PINS:
            pin = PWMOut(pin, duty_cycle=0, frequency=100)
            self.leds.append(pin)

    def set_colors(self, colors):
        for i in range(len(self.leds)):
            self.leds[i].duty_cycle = colors[i]
