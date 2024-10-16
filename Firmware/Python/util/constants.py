from adafruit_hid.keycode import Keycode
import board

# KEYPAD
ROW_PINS = [board.GP2, board.GP3, board.GP4, board.GP5]
COL_PINS = [board.GP6, board.GP7, board.GP8]
ENCODER_PIN_1 = board.GP10
ENCODER_PIN_2 = board.GP11
BLUE_LED = board.GP19
GREEN_LED = board.GP20
RED_LED = board.GP21

HARDWARE_KEYS = [
    Keycode.ONE,
    Keycode.TWO,
    Keycode.THREE,
    Keycode.FOUR,
    Keycode.FIVE,
    Keycode.SIX,
    Keycode.SEVEN,
    Keycode.EIGHT,
    Keycode.NINE,
    Keycode.KEYPAD_PLUS,
    Keycode.KEYPAD_ASTERISK,
    Keycode.ZERO,
]

# LED
LED_INTENSITY = int(65535 / 100)
LED_PINS = [BLUE_LED, GREEN_LED, RED_LED]

# ENCODER
ENCODER_CLOCK_KEYCODE = 13
ENCODER_ANTICLOCK_KEYCODE = 14
