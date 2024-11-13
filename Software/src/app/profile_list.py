from app.list_item import ListItem
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class ProfileList(QWidget):
    edit = Signal(dict)
    delete = Signal(str)

    def __init__(self, profiles, parent=None):
        super(ProfileList, self).__init__(parent)

        self.profiles = profiles

        layout = QVBoxLayout(self)

        label = QLabel("Applications")
        layout.addWidget(label)

        for index, profile in enumerate(profiles):
            item = ListItem(profile.name, self)
            item.edit_button.clicked.connect(lambda _c, i=index: self.edit_clicked(i))
            layout.addWidget(item)

        button = QPushButton("+")
        layout.addWidget(button)
        button.clicked.connect(self.add_app)

        self.setLayout(layout)

    @Slot()
    def add_app(self):
        print("Add app")

    @Slot()
    def edit_clicked(self, index):
        self.edit.emit({"index": index})
