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
    print(valuesSent)
    MOUSE.scroll(int(valuesSent[0]), int(valuesSent[1]))


def communication_handler(serialcomm, shortcuts):
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
