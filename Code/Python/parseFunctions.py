import pynput
import subprocess


# Start keyboard and mouse controllers, key and button classes
KEYBOARD = pynput.keyboard.Controller()
MOUSE = pynput.mouse.Controller()
KBKEY = pynput.keyboard.Key
MSBUTTON = pynput.mouse.Button

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


