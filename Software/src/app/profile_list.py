from app.list_item import ListItem
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel


class ProfileList(QWidget):
    edit = Signal(dict)
    delete = Signal(str)

    def __init__(self, profiles, current_profile, parent=None):
        super(ProfileList, self).__init__(parent)

        self.profiles = profiles
        self.current_profile = current_profile

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
        layout = QVBoxLayout(self)

        label = QLabel("Applications")
        layout.addWidget(label)

        for name, data in profiles.items():
            item = ListItem(data["name"], name, self)
            item.edit_button.clicked.connect(lambda: self.edit_clicked(data))
            item.delete_button.clicked.connect(self.delete_clicked)

            layout.addWidget(item)

        button = QPushButton("+")
        layout.addWidget(button)
        button.clicked.connect(self.add_app)

        self.setLayout(layout)

    @Slot()
    def add_app(self):
        print("Add app")

    @Slot()
    def edit_clicked(self, profile):
        print("Editing", profile)
        self.edit.emit(profile)

    @Slot()
    def delete_clicked(self, profile):
        print("Deleting", profile)
        self.delete.emit(profile)
