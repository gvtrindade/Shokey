import json

from util.app_command import AppCommand


class Actions:
    def __init__(self, shortcuts):
        self.shortcuts = shortcuts

    def parse_data(self, data):
        try:
            return json.loads(data)
        except json.decoder.JSONDecodeError:
            # If not json, data should be a shortcut
            return data

    def execute_action(self, data):
        app_command = AppCommand(data)

        if app_command.app == "shortcut":
            if app_command.action == "load":
                self.shortcuts.shortcuts = app_command.data
