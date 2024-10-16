import serial

def establish_connection(port):
    return serial.Serial(f"/dev/{port}", 115200, timeout=1000)


def send_serial_msg(serialcomm, msg):
    serialcomm.write(msg.encode())
