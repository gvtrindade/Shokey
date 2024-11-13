import time
import serial
import serial.tools.list_ports

from util.actions import Actions
from util.shortcuts import Shortcuts

# Define to which port the keypad is connected
VENDORID = 9026  # converted from hexadecimal: 0x2342
PRODUCTID = 32825  # converted from hexadecimal:0x8039


class Communication:
    def __init__(self) -> None:
        self.retry_timeout = 0.8
        self.baudrate = 115200
        self.serialcomm = None

        self.shortcuts = Shortcuts()
        self.actions = Actions(self.shortcuts)

    def search_port(self):
        while not self.find_used_port():
            self.find_used_port()
            time.sleep(self.retry_timeout)

    def ports_in_use(self):
        return serial.tools.list_ports.comports()

    def test_connection(self):
        portFound = any(
            (p.vid == VENDORID and p.pid == PRODUCTID) for p in self.ports_in_use()
        )
        return portFound

    def find_used_port(self):
        for p in self.ports_in_use():
            # TODO set to "Shokey" and get correct port
            if p.description == "Pico - CircuitPython CDC2 control":
                return p.name

        return False

    def establish_connection(self, port):
        time.sleep(2)
        self.serialcomm = serial.Serial(f"/dev/{port}", self.baudrate, timeout=1000)
        self.serialcomm.reset_input_buffer()
        self.serialcomm.reset_output_buffer()

    def send_data(self, msg):
        self.serialcomm.write(msg.encode())

    def read_data(self):
        return self.serialcomm.read_until(b"\n").decode()
