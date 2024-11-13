import pynput
import subprocess


class Shortcuts:
    def __init__(self) -> None:
        self.shortcuts = {}
        self.current_profile = "default"

        self.keyboard = pynput.keyboard.Controller()
        self.keyboard_key = pynput.keyboard.Key
        self.mouse = pynput.mouse.Controller()
        self.mouse_button = pynput.mouse.Button

    def execute_shortcut(self, command):
        # Shortcuts come in the format "00, 0\n"(key number, state)
        shortcuts = self.shortcuts[self.current_profile]
        shortcut = shortcuts["shortcuts"][int(command[:2])]
        state = int(command[4])

        if shortcut != -1:
            if shortcut.startswith("key"):
                self.key_command(shortcut[4:], state)
            elif shortcut.startswith("combo"):
                comboToPress = shortcut[6:].split("+")
                self.combo_command(comboToPress, state)
            elif shortcut.startswith("txt"):
                self.txt_command(shortcut[4:], state)
            elif shortcut.startswith("link"):
                self.link_command(shortcut[5:], state)
            elif shortcut.startswith("scroll"):
                scrollDirections = shortcut[7:].split(",")
                self.scroll_command(scrollDirections, state)

    def key_command(self, pressed_key, state):
        key_code = (
            getattr(self.keyboard_key, pressed_key)
            if len(pressed_key) > 1
            else pressed_key
        )
        if state:
            self.keyboard.press(key_code)
        else:
            self.keyboard.release(key_code)

    def combo_command(self, comboToPress, state):
        if state:
            firstKey = self.keyboard.pressed(
                getattr(self.keyboard_key, comboToPress[0])
            )
            lastKey = comboToPress[len(comboToPress) - 1]
            if len(comboToPress) > 2:
                secondKey = self.keyboard.pressed(
                    getattr(self.keyboard_key, comboToPress[1])
                )
                with firstKey:
                    with secondKey:
                        self.key_command(lastKey, 1)
            else:
                with firstKey:
                    self.key_command(lastKey, 1)

    def txt_command(self, txtSent, state):
        if state:
            self.keyboard.type(txtSent)

    def link_command(self, linkSent, state):
        if state:
            subprocess.Popen(linkSent)

    def scroll_command(self, valuesSent, state):
        if state:
            self.mouse.scroll(int(valuesSent[0]), int(valuesSent[1]))
