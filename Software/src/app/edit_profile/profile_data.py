from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ProfileData(QWidget):
    def __init__(self, parent=None):
        super(ProfileData, self).__init__(parent)

        self.combo_items = ["0", "50", "100", "150", "200", "250"]

        self.layout = QVBoxLayout()

        self.label = QLabel("Profile")
        self.layout.addWidget(self.label)

        # Profile name
        self.edit = QLineEdit("Default")
        self.title = QLabel("Name:")
        self.title.setBuddy(self.edit)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.edit)

        # Profile color
        # self.colors_component = self.build_color_component()
        widget = QWidget()
        layout = QGridLayout()

        self.color_box = QWidget(self)
        self.color_box.setStyleSheet("background-color: #000")
        layout.addWidget(self.color_box, 0, 0, 3, 1)

        combo_box_width = 100

        # Red
        self.red_combobox = QComboBox()
        self.red_combobox.setMaximumWidth(combo_box_width)
        self.red_combobox.addItems(self.combo_items)
        self.red_combobox.setCurrentIndex(0)

        red_label = QLabel("Red:")
        red_label.setBuddy(self.red_combobox)

        layout.addWidget(red_label, 0, 3)
        layout.addWidget(self.red_combobox, 0, 4)

        # Green
        self.green_combobox = QComboBox()
        self.green_combobox.setMaximumWidth(combo_box_width)
        self.green_combobox.addItems(self.combo_items)
        self.green_combobox.setCurrentIndex(0)

        green_label = QLabel("Green:")
        green_label.setBuddy(self.green_combobox)

        layout.addWidget(green_label, 1, 3)
        layout.addWidget(self.green_combobox, 1, 4)

        # Blue
        self.blue_combobox = QComboBox()
        self.blue_combobox.setMaximumWidth(combo_box_width)
        self.blue_combobox.addItems(self.combo_items)
        self.blue_combobox.setCurrentIndex(0)

        blue_label = QLabel("Blue:")
        blue_label.setBuddy(self.blue_combobox)

        layout.addWidget(blue_label, 2, 3)
        layout.addWidget(self.blue_combobox, 2, 4)

        # Add colors widget
        widget.setLayout(layout)
        self.layout.addWidget(widget)

        # Buttons
        self.save_button = QPushButton("Save")
        self.layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete")
        self.layout.addWidget(self.delete_button)

        self.cancel_button = QPushButton("Cancel")
        self.layout.addWidget(self.cancel_button)

        self.setLayout(self.layout)

    def change_profile(self, profile):
        self.label.setText(profile.name)
        self.edit.setText(profile.name)
        self.color_box.setStyleSheet(f"background-color: #{profile.color}")

        self.red_combobox.setCurrentIndex(self.get_color(profile.color[0:2]))
        self.green_combobox.setCurrentIndex(self.get_color(profile.color[2:4]))
        self.blue_combobox.setCurrentIndex(self.get_color(profile.color[4:6]))

    def get_color(self, color):
        number = int(color, 16)
        return min(enumerate(self.combo_items), key=lambda x: abs(int(x[1]) - number))[
            0
        ]

    # def build_color_component(self):
    #     widget = QWidget()
    #     layout = QGridLayout()

    #     color_box = QWidget(self)
    #     color_box.setStyleSheet("background-color: #000")
    #     layout.addWidget(self.color_box, 0, 0, 3, 1)

    #     for index, color in enumerate(["Red", "Green", "Blue"]):
    #         style_combobox = QComboBox()
    #         style_combobox.setMaximumWidth(50)
    #         style_combobox.addItems()
    #         style_combobox.setCurrentIndex(0)

    #         style_label = QLabel(f"{color}:")
    #         style_label.setBuddy(style_combobox)

    #         layout.addWidget(style_label, index, 3)
    #         layout.addWidget(style_combobox, index, 4)

    #     widget.setLayout(layout)
    #     self.layout.addWidget(widget)
