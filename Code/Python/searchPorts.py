import serial.tools.list_ports  # Imported from pyserial

# Define to which port the keypad is connected
VENDORID = 9026  # converted from hexadecimal: 0x2342
PRODUCTID = 32825  # converted from hexadecimal:0x8039


def ports_in_use():
    return serial.tools.list_ports.comports()


def test_connection():
    portFound = any((p.vid == VENDORID and p.pid == PRODUCTID)
                    for p in ports_in_use())
    return portFound


def find_used_port():
    for p in ports_in_use():
        if (p.vid == VENDORID and p.pid == PRODUCTID):
            return p.name

    return False