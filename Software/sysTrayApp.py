from infi.systray import SysTrayIcon
import subprocess


program_name = "notepad.exe"
file_name = "shortcuts.txt"

def open_shortcuts(systray):
  subprocess.Popen([program_name, file_name])

menu_options = (("Shortcuts", None, open_shortcuts), )
systray = SysTrayIcon("./assets/icon.ico" , "Shokey", menu_options)
systray.start()