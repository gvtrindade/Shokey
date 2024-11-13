from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Encoder(QWidget):
    def __init__(self, parent=None):
        super(Encoder, self).__init__(parent)
        self.button_codes = [9, 12, 13]

    def get_initial_and_shortcut(self, item):
        type = ""
        shortcut = ""
        if len(item) > 1:
            type, shortcut = item.split(".")
        return type.upper(), shortcut

    def change_profile(self, profile):
        layout = QVBoxLayout(self)

        for code in self.button_codes:
            button = QPushButton()

            initial, shortcut = self.get_initial_and_shortcut(profile.shortcuts[code])
            button.setToolTip(shortcut)
            button.setText(initial)

            layout.addWidget(button)

        self.setLayout(layout)
