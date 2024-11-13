from app.encoder import Encoder
from app.profile_data import ProfileData
from app.profile_list import ProfileList
from app.shokey import Shokey
from app.util.profile import get_profiles
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QLabel, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.profiles = get_profiles()
        self.current_profile = 0

        self.setWindowTitle("Shokey")
        self.setGeometry(100, 100, 800, 600)
        self.setMaximumHeight(600)
        self.setMaximumWidth(800)

        self.label = QLabel("Shokey")
        self._profile_list = ProfileList(self.profiles, self)
        self._profile_data = ProfileData(self.profiles[self.current_profile], self)
        self._encoder = Encoder(self)
        self._shokey = Shokey(self)

        self._profile_list.edit.connect(self.edit_profile)
        self._profile_data.cancel.connect(self.cancel_edit)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self._profile_list, 0, 0)

        self._main_widget = QWidget()
        self._main_widget.setLayout(self.layout)
        self.setCentralWidget(self._main_widget)

    @Slot()
    def edit_profile(self, data):
        self.change_profile(data["index"])
        self.toggle_profile_data(True)

    @Slot()
    def cancel_edit(self):
        self.toggle_profile_data(False)

    def change_profile(self, profile_index):
        self.current_profile = profile_index
        profile = self.profiles[profile_index]

        self._encoder.change_profile(profile)
        self._shokey.change_profile(profile)
        self._profile_data.change_profile(profile)

    def toggle_profile_data(self, show_data):
        if show_data:
            self.layout.addWidget(self._profile_data, 0, 0)
            self.layout.addWidget(self._encoder, 0, 1)
            self.layout.addWidget(self._shokey, 0, 2)

            self._profile_data.show()
            self._encoder.show()
            self._shokey.show()
            self._profile_list.hide()

            self.layout.removeWidget(self._profile_list)
        else:
            self.layout.addWidget(self._profile_list, 0, 0)

            self._profile_list.show()
            self._profile_data.hide()
            self._encoder.hide()
            self._shokey.hide()

            self.layout.removeWidget(self._profile_data)
            self.layout.removeWidget(self._encoder)
            self.layout.removeWidget(self._shokey)
