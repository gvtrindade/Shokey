import usb_cdc


class Communication:
    def __init__(self) -> None:
        self.serial = usb_cdc.data

    def ping_software(self):
        return self.serial.connected
    
    def write_data(self, key_event, encoder_event):
        if encoder_event:
            data = f"{encoder_event}, 1".encode()
        else:
            state = 1 if key_event.pressed else 0
            number = key_event.key_number
            data = f"{number}, {state}".encode()

        print(data)
        self.serial.write(data)

    def read_data(self):
        data = ""

        while self.serial.in_waiting > 0:
            data += self.serial.read(self.serial.in_waiting).decode("utf-8")

        return data if data != "" else None            
