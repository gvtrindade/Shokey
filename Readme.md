# ![Shokey icon](./Images/Shokey_Icon.png) Shokey

An Arduino based Shortcut Keypad and Python app.

- [Arduino](#arduino)
  - [Features](#features)
  - [Assembling the hardware](#assemling-the-hardware)
  - [Flashing the firmware](#flashing-the-firmware)
  - [Using your Shokey as a numeric keypad](#using-your-shokey-as-a-numeric-keypad)
- [Python](#python)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Shokey layout](#shokey-layout)
  - [Shortcut Editing](#shortcut-editing)
  - [Shortcut syntax](#shortcut-syntax)
  - [Custom keys](#custom-keys)
- [References](#references)


## Arduino

The hardware part was made using an Arduino Pro Micro, Cherry MX Brown Switches and 3D printed shell and keycaps.

### Features

- Can be used as a numeric keyboard in any device while not running the app
- Has a cool RGB LED, that changes color

### Assembling the hardware

1. Download and print the shell, keycaps and rotary encoder knob

2. Place all switches and screw in the rotary encoder in the top part of the shell

3. Solder the switches, rotary encoder and RGB LED to their respective pins in the Arduino, following the [wiring diagram](https://github.com/gvtrindade/Shokey/Code/Arduino/Wiring_Diagram.jpg)

4. Making sure to have no solder bridges between the board pins, connect the Arduino to the PC and [flash the firmware](#flashing-the-firmware)

5. While being extremely careful, close the shell, screw it and glue the rubber feet

### Flashing the firmware

1. Connect your Shokey to the computer

2. Make sure you have [Arduino IDE](https://www.arduino.cc/en/software) installed

3. In your Arduino IDE, go to Sketch/Include Library/Manage Libraries 

4. Search for and make sure that the Bounce2, Encoder, Keyboard and Keypad libraries are installed

5. [Download](https://github.com/gvtrindade/Shokey/releases) and unzip the **Firmware.zip** file

6. Copy the "hardware" folder into to your "Documents/Arduino" folder

7. Go back to the "Firmware" folder and open "Shokey/Shokey.ino"

8. Go to Tools/Board/gvtrindade-avr and select "Arduino Leonardo Shokey"

    8.1. If you don't find "gvtrindade-avr" inside the boards menu, go back to step 5 

9. Go to Tools/Ports and select the "COM" port in which the board is connected

    9.1. If there is an option listed with "(Arduino Leonardo)", select it and go to step 9

    9.2. Look at the number of the "COM" ports and disconnect your Shokey

    9.3. Go to Tools/Ports and take note of the port that disappeared
    
    9.3. Reconnect your Shokey and select the option that reapeared   

10. Go to Sketch/Upload

11. When the upload is complete, you can already use your Shokey as numeric keypad, but if you want to have the full shortcut experience, you'll have to install the application

### Using your Shokey as a numeric keypad

To use your Shokey as a numeric keypad, you just connect it to your device and start pressing the keys. 

Here's a layout of the keys in numeric keypad mode:

![Shokey layout in numeric keypad mode](./Images/Shokey_Numeric.png)

## Python

The app is a Windows System Tray app built with Infi's Systray and is used to send and edit the shortcuts

### Features

- Maps keystrokes, key combinations, writes text, opens programs and scroll pages
- Detects automatically whether a Shokey is connected to the PC
- Cute thunderstorm icon

### Installation

1. [Download](https://github.com/gvtrindade/Shokey/releases) and unzip the **Application.zip** file

2. Make sure your Shokey is connected

3. Open "Application/Shokey.exe"

### Usage

- While the app is open, there will be a cute thunderstorm icon in the bottom right of your taskbar:

    ![Taskbar icon](./Images/Taskbar_Icon.jpg)

- Double clicking it will open the "shortcuts.txt" file, allowing you to [edit your shortcuts](#shortcut-editing)
- Right clicking it will open a menu to open the Shortcuts file, About file or quit the app:

    ![Right clicked taskbar icon](./Images/Taskbar_Right_Click.jpg)
    

#### Shokey layout
The numbers go from 1 to 9, just like a numeric keyboard. The top keys are the `*` and `0`, from left to right.

The Shokey has 4 layers, each based on the RGB LED color (red, green, blue and white). 

The `*` key is used to change between layers.

![Shokey layer colors](./Images/Shokey_Layers.gif)

The rotary encoder is represented by three variables inside the "shortcuts.txt", `VU` (Volume Up), `VD` (Volume Down) and `E` (Encoder button)

![Shokey Encoder](./Images/Shokey_Encoder.gif)


#### Shortcut editing

In the "shortcuts.txt" is where all the magic happens, here is where you write the shortcuts that will be played when you press a key in your Shokey.

The file has 4 sets of lines, 1 for each color.

To add a shortcut you have to find the key that you want to press, based on the layout shown above, as well as the color and add the shortcut after the `;`, folowing the [shortcut syntax](#shortcut-syntax).

Eg.: `1R; key.a` is the number one key of the red layer and the shortcut to be executed is the key `a` on the keyboard.

After writing the desired shortcut, save the file and close it.

The change in the shortcut will only take effect after the second time the button is pressed.

#### Shortcut syntax

The shortcuts will only work if the corretct syntax is used, so if it does not work, open "shotcuts.txt" and check if it is correct.

There are examples of shortcuts in the file, but you can use this list to help you write your own:

- Key shortcut: key.*key*
- Combo of keys shortcut: combo.*key1*+*key2*
- Write text shortcut: txt.*text*
- Open a program shortcut: link.*full_exe_adress*
- Scroll the page shortcut: scroll.*horizontal value*, *vertical Value*

##### Example

    1R; key.a
    2G; combo.alt+f4
    3B; txt.Hello World
    4W; link.C:\Windows\System32\calc.exe
    ER; key.media_play_pause
    VUG; scroll.0,-1
    VDG; scroll.0,1

#### Custom keys
Some keys are special, the following list has some examples:
- key.media_play_pause, play and pause control
- key.media_volume_up, turn up the volume
- key.media_volume_down, turn down the volume
- combo.ctrl+c, combo.ctrl+v

Here are other keys, some 
- f2, f5, space, escape, delete, home, end
- ctrl, alt, shift, cmd (windows key)
- up, down, left, right
- [More custom keys](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)

## References

- [Programmable Macropad v2 - 
Tiny Boat Productions](https://www.instructables.com/Programmable-Macropad-V2/)
- [MIDI device name - musinou](http://liveelectronics.musinou.net/MIDIdeviceName.php)
- [Bounce2](https://www.arduino.cc/reference/en/libraries/bounce2/)
- [Encoder](https://www.arduino.cc/reference/en/libraries/encoder/)
- [Keyboard](https://www.arduino.cc/reference/en/libraries/keyboard/)
- [Keypad](https://www.arduino.cc/reference/en/libraries/keypad/)
- [Pynput](https://pypi.org/project/pynput/)
- [Pyserial](https://pypi.org/project/pyserial/)
- [Systray](https://github.com/Infinidat/infi.systray)
- Icons made by Freepik from flaticon.com
