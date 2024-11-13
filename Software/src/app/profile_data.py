from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Slot, Signal


class ProfileData(QWidget):
    cancel = Signal(str)

    def __init__(self, profile, parent=None):
        super(ProfileData, self).__init__(parent)
        self.profile = profile

        # self.setGeometry(100, 50, 200, 400)
        # self.setObjectName("appList")
        # self.setStyleSheet(
        #     """
        #         QWidget#appList {
        #             border: 3px solid #D9D9D9;
        #             border-radius: 20px;
        #         }
        #     """
        # )
        self.layout = QVBoxLayout(self)

        label = QLabel("Profile Data")
        self.layout.addWidget(label)

        self.title = QLabel(profile["name"])
        self.layout.addWidget(self.title)

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
        self.title.setText(profile["name"])

    @Slot()
    def save_clicked(self):
        print("Saving", self.profile)

    @Slot()
    def delete_clicked(self):
        print("Deleting", self.profile)

    @Slot()
    def cancel_clicked(self):
        print("Canceling", self.profile)
        self.cancel.emit(self.profile)
