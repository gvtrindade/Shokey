import os

def set_shortcuts(shortcuts):
    with open(f"{os.getcwd()}/assets/shortcuts.txt", "rt") as file:
        for line in file:
            if line.strip():
                key, val = line.strip().split(";")
                shortcuts[key.strip()] = val.strip()