class Profile:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.shortcuts = data["shortcuts"]
        self.color = data["color"]

    def get_slug(self):
        return self.name.lower().replace(" ", "_")

    def to_dict(self):
        return {"name": self.name, "shortcuts": self.shortcuts, "color": self.color}
