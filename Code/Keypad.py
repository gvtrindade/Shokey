import sys
import subprocess
import os
import time
import pynput
import serial.tools.list_ports  # Imported from pyserial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Start keyboard and mouse controllers, key and button classes
KEYBOARD = pynput.keyboard.Controller()
MOUSE = pynput.mouse.Controller()
KBKEY = pynput.keyboard.Key
MSBUTTON = pynput.mouse.Button

# Get shortcut list from file
shortcuts = {}
currentDirectory = os.getcwd() + '\Code\shortcuts.txt'
def set_shortcuts():
    file = open(currentDirectory, 'rt')
    for line in file:
        if line.strip():
            key, val = line.strip().split(';')
            shortcuts[key.strip()] = val.strip()


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


# Establish serial connection between the arduino and the app
def establish_connection(port):
    return serial.Serial(port, 9600)


def send_serial_msg(serialcomm, msg):
    serialcomm.write(msg.encode())


# Handle the type of command to be executed
def key_command(pressedKey):
    if (len(pressedKey) > 1):
        KEYBOARD.tap(getattr(KBKEY, pressedKey))
    else:
        KEYBOARD.tap(pressedKey)


def combo_command(comboToPress):
    firstKey = KEYBOARD.pressed(getattr(KBKEY, comboToPress[0]))
    lastKey = comboToPress[len(comboToPress) - 1]
    if (len(comboToPress) > 2):
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
    print(valuesSent)
    MOUSE.scroll(int(valuesSent[0]), int(valuesSent[1]))


def communication_handler(serialcomm):
    set_shortcuts()
    var = serialcomm.readline().decode('ascii').strip()
    shortcut = shortcuts.get(var, -1)

    if (var[0] == '0'):
        print('Closing app...')
        send_serial_msg(serialcomm, 'O')
        serialcomm.close()
        sys.exit()

    elif (shortcut != -1):

        if (shortcut[:3] == 'key'):
            key_command(shortcut[4:])

        if (shortcut[:5] == 'combo'):
            comboToPress = shortcut[6:].split('+')
            combo_command(comboToPress)

        if (shortcut[:3] == 'txt'):
            txt_command(shortcut[4:])

        if (shortcut[:4] == 'link'):
            link_command(shortcut[5:])

        if (shortcut[:6] == 'scroll'):
            scrollDirections = shortcut[7:].split(',')
            scroll_command(scrollDirections)
    del var


#Searching for the arduino and updating the communication 
sleep_amount = 0.8

while (not find_used_port()):
    find_used_port()
    time.sleep(sleep_amount)

def update_communication():

    serialcomm = establish_connection(find_used_port())
    send_serial_msg(serialcomm, 'I')

    while True:
        try:
            communication_handler(serialcomm)

        except SystemExit:
            break

        except:
            print(sys.exc_info()[0])
            find_used_port()
            if(find_used_port()):
                update_communication()
            time.sleep(sleep_amount)


update_communication()
