class AppCommand:
    def __init__(self, data):
        self.app = data["app"]
        self.action = data["action"]
        self.data = data["data"]
