import usb_hid
from adafruit_hid.keyboard import Keyboard


class KeypadApp:
    def __init__(self, hardware_keys):
        self.keyboard = Keyboard(usb_hid.devices)
        self.hardware_keys = hardware_keys

    def press_key(self, event):
        key = self.hardware_keys[event.key_number]
        if event.pressed:
            self.keyboard.press(key)
        else:
            self.keyboard.release(key)
