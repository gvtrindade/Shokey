import os
import time
import serial.tools.list_ports


# Get shortcut list from file
shortcuts = {}


def set_shortcuts():
    file = open(
        "/home/gabriel/Documents/Stuff/Shokey/Code/Software/assets/shortcuts.txt", "rt"
    )
    for line in file:
        if line.strip():
            key, val = line.strip().split(";")
            shortcuts[key.strip()] = val.strip()


def ports_in_use():
    return serial.tools.list_ports.comports()


def find_used_port():
    for p in ports_in_use():
        if p.manufacturer == "Raspberry Pi":  # TODO set to "Shokey"
            return p.name

    return False


###############
###############
import pynput
import subprocess

# Start keyboard and mouse controllers, key and button classes
KEYBOARD = pynput.keyboard.Controller()
MOUSE = pynput.mouse.Controller()
KBKEY = pynput.keyboard.Key
MSBUTTON = pynput.mouse.Button


# Handle the type of command to be executed
def key_command(pressedKey):
    if len(pressedKey) > 1:
        KEYBOARD.tap(getattr(KBKEY, pressedKey))
    else:
        KEYBOARD.tap(pressedKey)


def combo_command(comboToPress):
    firstKey = KEYBOARD.pressed(getattr(KBKEY, comboToPress[0]))
    lastKey = comboToPress[len(comboToPress) - 1]
    if len(comboToPress) > 2:
        secondKey = KEYBOARD.pressed(getattr(KBKEY, comboToPress[1]))
        with firstKey:
            with secondKey:
                key_command(lastKey)
    else:
        with firstKey:
            key_command(lastKey)


def txt_command(txtSent):
    KEYBOARD.type(txtSent)


def link_command(linkSent):
    subprocess.Popen(linkSent)


def scroll_command(valuesSent):
    MOUSE.scroll(int(valuesSent[0]), int(valuesSent[1]))


###############
###############
# Establish serial connection between the arduino and the app
def establish_connection(port):
    return serial.Serial(f"/dev/{port}", 115200, timeout=1000)


def send_serial_msg(serialcomm, msg):
    print("Sending message")
    serialcomm.write(msg.encode())
    received_message = serialcomm.readline().decode().strip()
    print(received_message)


def communication_handler(serialcomm):
    # set_shortcuts()
    received_message = serialcomm.readline().decode().strip()
    shortcut = shortcuts.get(received_message, -1)

    if shortcut != -1:

        if shortcut[:3] == "key":
            key_command(shortcut[4:])

        if shortcut[:5] == "combo":
            comboToPress = shortcut[6:].split("+")
            combo_command(comboToPress)

        if shortcut[:3] == "txt":
            txt_command(shortcut[4:])

        if shortcut[:4] == "link":
            link_command(shortcut[5:])

        if shortcut[:6] == "scroll":
            scrollDirections = shortcut[7:].split(",")
            scroll_command(scrollDirections)
    del received_message


# Searching for the arduino and updating the communication
sleep_amount = 0.8

while not find_used_port():
    find_used_port()
    time.sleep(sleep_amount)


def update_communication():
    global serialcomm
    used_port = find_used_port()
    serialcomm = establish_connection(used_port)
    send_serial_msg(serialcomm, "I")
    set_shortcuts()

    while True:
        try:
            communication_handler(serialcomm)

        except Exception as e:
            print(e)
            find_used_port()
            if find_used_port():
                update_communication()
            time.sleep(sleep_amount)


###############
###############
# from infi.systray import SysTrayIcon
# import subprocess

# program_name = "notepad.exe"
# shortcuts_file = "./assets/shortcuts.txt"
# about_file = "./assets/About.txt"

# def open_shortcuts(systray):
#     subprocess.Popen([program_name, shortcuts_file])

# def open_about(systray):
#     subprocess.Popen([program_name, about_file])

# def exit_app(systray):
#     send_serial_msg(serialcomm, 'O')
#     serialcomm.close()
#     os._exit(1)

# menu_options = (("Shortcuts", None, open_shortcuts), ("About", None, open_about),)
# systray = SysTrayIcon("./assets/icon.ico" , "Shokey", menu_options, on_quit=exit_app)


# systray.start()

update_communication()
