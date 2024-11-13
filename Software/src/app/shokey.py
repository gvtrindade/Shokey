from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton


class Shokey(QWidget):
    def __init__(self, parent=None):
        super(Shokey, self).__init__(parent)
        self._encoder_key_code = 9
        self.rows = 4
        self.cols = 3

    def get_initial_and_shortcut(self, item):
        type = ""
        shortcut = ""
        if len(item) > 1:
            type, shortcut = item.split(".")
        return type.upper(), shortcut

    def change_profile(self, profile):
        layout = QGridLayout(self)

        counter = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if counter != self._encoder_key_code:
                    button = QPushButton()

                    initial, shortcut = self.get_initial_and_shortcut(
                        profile.shortcuts[counter]
                    )
                    button.setToolTip(shortcut)
                    button.setText(initial)

                    layout.addWidget(button, self.rows - row, col)
                counter += 1
        self.setLayout(layout)
