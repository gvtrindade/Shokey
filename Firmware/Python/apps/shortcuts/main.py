import json


class ShortcutsApp:
    def __init__(self, leds):
        self.profiles = {}
        self.current_profile = None
        self.leds = leds

        self.load_profiles()
        self.change_profile("default")

    def load_profiles(self):
        with open("apps/shortcuts/profiles.json", "r") as file:
            self.profiles = json.loads(file.read())

    def save_profiles(self, profiles):
        with open("apps/shortcuts/profiles.json", "w") as file:
            file.write(json.dumps(profiles))
        self.load_profiles()

    def change_profile(self, profile_name):
        try:
            new_profile = self.profiles[profile_name]
        except KeyError:
            new_profile = self.profiles["default"]
            
        self.current_profile = new_profile
        self.leds.set_colors(new_profile["colors"])
