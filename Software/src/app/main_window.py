from app.edit_profile.edit_profile import EditProfile
from app.profile_list.profile_list import ProfileList
from app.util.profile import get_profiles
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QLabel, QMainWindow, QWidget


"""
    Main window
    - Manages shown screen
    - Maintains list of profiles
    - Keeps track of current profile
"""


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Window Properties
        self.setWindowTitle("Shokey")
        self.setGeometry(100, 100, 800, 600)
        self.setMaximumHeight(600)
        self.setMaximumWidth(800)

        # Profile Management
        self.profiles = get_profiles()
        self.current_profile = 0

        # Components
        self._profile_list = ProfileList(self.profiles, self)
        self._profile_list.edit.connect(self.edit_profile)

        self._edit_profile = EditProfile(self.profiles[self.current_profile], self)
        self._edit_profile.cancel.connect(self.cancel_edit)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self._profile_list, 0, 0)

        self._main_widget = QWidget()
        self._main_widget.setLayout(self.layout)
        self.setCentralWidget(self._main_widget)

    @Slot()
    def edit_profile(self, data):
        self.change_profile(data["index"])
        self.change_view("edit_profile")

    @Slot()
    def cancel_edit(self):
        self.change_view("list")

    def change_profile(self, profile_index):
        self.current_profile = profile_index
        profile = self.profiles[profile_index]

        self._edit_profile.change_profile(profile)

    def change_view(self, show_data):
        match show_data:
            case "edit_profile":
                self.layout.addWidget(self._edit_profile, 0, 0)

                self._edit_profile.show()
                self._profile_list.hide()

                self.layout.removeWidget(self._profile_list)

            case "list":
                self.layout.addWidget(self._profile_list, 0, 0)

                self._profile_list.show()
                self._edit_profile.hide()

                self.layout.removeWidget(self._edit_profile)

            case _:
                raise Exception("Invalid view type")
