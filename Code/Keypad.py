import sys
import subprocess 
import pynput 
import serial.tools.list_ports # Imported from pyserial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#Start keyboard and mouse controllers, key and button classes
KEYBOARD = pynput.keyboard.Controller()
MOUSE = pynput.mouse.Controller()
KBKEY = pynput.keyboard.Key
MSBUTTON = pynput.mouse.Button

#Define to which port the keypad is connected 
VENDORID = 9026 #converted from hexadecimal: 0x2342
PRODUCTID = 32825 #converted from hexadecimal:0x8039

def ports_in_use():
    return serial.tools.list_ports.comports()


def test_connection():
    portFound = any((p.vid == VENDORID and p.pid == PRODUCTID) for p in ports_in_use())
    return portFound


def find_used_port():
    for p in ports_in_use():
        if (p.vid == VENDORID and p.pid == PRODUCTID):
            return p.name            


#Get shortcut list from file
shortcuts = {}
def define_values():
    file = open('shortcuts.txt','rt')
    for line in file:
        if line.strip():
            key, val = line.strip().split(';')
            shortcuts[key.strip()] = val.strip()


#Functions to handle the type of command to be executed
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
    MOUSE.scroll(int(valuesSent[0]),int(valuesSent[1]))


#Handle the serial connection between the arduino and the program 
def establish_connection(port):
    return serial.Serial(port, 9600)


def send_serial_msg(msg):
    serialcomm.write(msg.encode())


serialcomm = establish_connection(find_used_port())
send_serial_msg('I')

class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Shokey')
        menu = QMenu(parent)
        open_app = menu.addAction("Exit")
        open_app.triggered.connect(self.exit_function)

        menu.addSeparator()
        self.setContextMenu(menu)

    def exit_function(self):
        sys.exit()

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    tray_icon = SystemTrayIcon(QIcon("icon.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


while True:

    define_values()
    var = serialcomm.readline().decode('ascii').strip()
    shortcut = shortcuts.get(var, -1)

    if (var[0] == '0'):
        send_serial_msg('O')
        serialcomm.close()
        sys.exit()

    if shortcut != -1:

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
