# Shokey

An Arduino based Shortcut Keypad and Python app.

- [Arduino](#arduino)
  - [Features](#features)
  - [Assembling the hardware](#assemling-the-hardware)
  - [Flashing the software](#flashing-the-software)
- [Python](#python)
  - [Features](#features)
  - [Installation](#installation)
  - [Shortcut syntax](#shortcut-syntax)
  - [Custom keys](#custom-keys)
- [References](#references)


## Arduino

The hardware part was made using an Arduino Pro Micro, Cherry MX Brown Switches and 3D printed shell and keycaps.

### Features

- Can be used as a numeric keyboard in any device while not running the app
- Has cool a RGB LED, that changes color

### Assembling the hardware

1. Download and print the shell, keycaps and rotary encoder knob

2. Place all switches and srew in the rotary encoder in the top part of the shell

3. Solder the switches, rotary encoder and RGB LED to their respective pins in the Arduino, following the Wiring Diagram

4. Making sure to have no solder bridges between the pins, connect the Arduino to the PC and [flash the software](#flashing-the-software)

5. While being extremely careful, close the shell, screw the screws and glue the rubber feet

### Flashing the software

1. Make sure you have [Arduino IDE](https://www.arduino.cc/en/software) installed

2. [Download](https://github.com/gvtrindade/Shokey/releases) the **Arduino.zip** file and copy the "Arduino" folder to your "Documents" folder

3. Open Shokey/Shokey.ino

4. Go to Tools/Board/gvtrindade-avr and select "Arduino Leonardo Shokey"

5. Go to Tools/Ports and select the port in which the board is connected

6. Press the Upload

## Python

The app is a Windows System Tray app built with Infi's Systray and is used to send and edit the shortcuts

### Features

- Maps keystrokes, key combinations, writes text, opens programs and scroll pages
- Detects automatically whether a Shokey is connected to the PC
- Cute thunderstorm icon

### Installation

1. [Download](https://github.com/gvtrindade/Shokey/releases) the **Application.zip** file

2. Connect your Shokey

3. Run the app

### Usage

- While the app is open, there will be an icon in the bottom left of your taskbar
- It can be double clicked to open the shortcuts.txt file
- When altered, the shortcut will update automatically after the first press, not needing to reset the app

#### Shortcut syntax

- To press a key: key.*key*
- To press a combo of keys: combo.*key1*+*key2*
- To send a text: txt.*text*
- To open a program: link.*full exe adress*
- To scroll the page: scroll.*horizontal value*, *vertical Value*

##### Example

    1R; key.a
    2R; combo.alt+f4
    3R; txt.Hello World
    4R; link.C:\Windows\System32\calc.exe
    5R; scroll.0,1

#### Custom keys
- media_play_pause, media_volume_up, media_volume_down
- f2, f5, space, esc, delete, home, end
- ctrl, alt, shift, cmd (windows key)
- up, down, left, right
- [More custom keys](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)

## References

- https://www.instructables.com/Programmable-Macropad-V2/
- http://liveelectronics.musinou.net/MIDIdeviceName.php
- https://www.arduino.cc/reference/en/libraries/bounce2/
- https://www.arduino.cc/reference/en/libraries/encoder/
- https://www.arduino.cc/reference/en/libraries/keyboard/
- https://www.arduino.cc/reference/en/libraries/keypad/
- https://pypi.org/project/pynput/
- https://pypi.org/project/pyserial/
- https://github.com/Infinidat/infi.systray
- Icons made by Freepik from flaticon.com
