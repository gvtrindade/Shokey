import json
from time import sleep

from util.leds import Leds
from util.rotary_encoder import Encoder
from util.serial_comm import Communication
from util.constants import (
    HARDWARE_KEYS,
    ROW_PINS,
    COL_PINS,
)
from keypad import KeyMatrix
from apps.shortcuts.main import ShortcutsApp
from apps.keypad.main import KeypadApp
from util.serial_data import SerialData


# Hardware setup
key_matrix = KeyMatrix(row_pins=ROW_PINS, column_pins=COL_PINS, columns_to_anodes=True)
encoder = Encoder()
serial_comm = Communication()
leds = Leds()


# Apps setup
current_app = "keypad"
keypad = KeypadApp(HARDWARE_KEYS)
shortcuts = ShortcutsApp(leds)

with open("apps/index.json", "r") as file:
    app_list = json.loads(file.read())

while True:
    key_event = key_matrix.events.get()
    encoder_event = encoder.update()
    software_mode = serial_comm.ping_software()

    serial_data = serial_comm.read_data()

    if serial_data:
        try:
            data = SerialData(serial_data)
            if data.app == "shortcut":
                if data.action == "change":
                    shortcuts.change_profile(data.data)
                elif data.action == "save":
                    shortcuts.save_profiles(data.data)
        except Exception as e:
            print(e)
            continue

    if key_event or encoder_event:
        if software_mode:
            if current_app != "shortcuts":
                current_app = "shortcuts"
            serial_comm.write_data(key_event, encoder_event)
        elif current_app == "keypad":
            keypad.press_key(key_event)
        else:
            pass

    sleep(0.01)
