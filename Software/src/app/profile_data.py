from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Slot, Signal


class ProfileData(QWidget):
    cancel = Signal(str)

    def __init__(self, profile, parent=None):
        super(ProfileData, self).__init__(parent)
        self.profile = profile

        self.layout = QVBoxLayout(self)

        label = QLabel("Profile Data")
        self.layout.addWidget(label)

        self.title = QLabel(profile.name)
        self.layout.addWidget(self.title)

        self.color_box = QWidget(self)
        self.color_box.setStyleSheet(f"background-color: #{profile.color}")
        self.layout.addWidget(self.color_box)

        # self._style_combobox = QComboBox()
        # init_widget(self._style_combobox, "styleComboBox")
        # self._style_combobox.addItems(style_names())

        # style_label = QLabel("Style:")
        # init_widget(style_label, "style_label")
        # style_label.setBuddy(self._style_combobox)

        self.setLayout(self.layout)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_clicked)
        self.layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_clicked)
        self.layout.addWidget(self.delete_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.layout.addWidget(self.cancel_button)

        self.setLayout(self.layout)

    def change_profile(self, profile):
        self.profile = profile
        self.title.setText(profile.name)
        self.color_box.setStyleSheet(f"background-color: #{profile.color}")

    @Slot()
    def save_clicked(self):
        print("Saving", self.profile)

    @Slot()
    def delete_clicked(self):
        print("Deleting", self.profile)

    @Slot()
    def cancel_clicked(self):
        self.cancel.emit(True)
