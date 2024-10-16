import rotaryio
from util.constants import (
    ENCODER_ANTICLOCK_KEYCODE,
    ENCODER_CLOCK_KEYCODE,
    ENCODER_PIN_1,
    ENCODER_PIN_2,
)


class Encoder:
    def __init__(self):
        self.last_position = 0
        self.encoder = rotaryio.IncrementalEncoder(ENCODER_PIN_1, ENCODER_PIN_2)

    def update(self):
        position = self.encoder.position
        last_position = self.last_position
        encoder_changed = position != last_position
        self.last_position = position

        if encoder_changed:
            return self.get_encoder_key_number(position, last_position)
        return None

    def get_encoder_key_number(self, encoder_position, encoder_last_position):
        if encoder_position > encoder_last_position:
            return ENCODER_CLOCK_KEYCODE
        elif encoder_position < encoder_last_position:
            return ENCODER_ANTICLOCK_KEYCODE
