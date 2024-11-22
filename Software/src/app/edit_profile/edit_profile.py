from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Signal, Slot

from app.edit_profile.encoder import Encoder
from app.edit_profile.profile_data import ProfileData
from app.edit_profile.shokey import Shokey


class EditProfile(QWidget):
    cancel = Signal(str)

    def __init__(self, profile, parent=None):
        super(EditProfile, self).__init__(parent)

        self.profile = profile

        self._profile_data = ProfileData(self)
        self._profile_data.save_button.clicked.connect(self.save_clicked)
        self._profile_data.delete_button.clicked.connect(self.delete_clicked)
        self._profile_data.cancel_button.clicked.connect(self.cancel_clicked)

        self._encoder = Encoder(self)
        self._shokey = Shokey(self)

        self.layout = QHBoxLayout(self)

        self.layout.addWidget(self._profile_data)
        self.layout.addWidget(self._encoder)
        self.layout.addWidget(self._shokey)

        self.setLayout(self.layout)

    def change_profile(self, profile):
        self.profile = profile

        self._profile_data.change_profile(profile)
        self._encoder.change_profile(profile)
        self._shokey.change_profile(profile)

    @Slot()
    def save_clicked(self):
        print("Saving", self.profile)

    @Slot()
    def delete_clicked(self):
        print("Deleting", self.profile)

    @Slot()
    def cancel_clicked(self):
        self.cancel.emit(True)
