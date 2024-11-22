from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QListView
from PySide6.QtGui import QStandardItem, QStandardItemModel

from app.edit_profile.list_item import ListItem


class ProfileList(QWidget):
    edit = Signal(dict)
    delete = Signal(str)

    def __init__(self, profiles, parent=None):
        super(ProfileList, self).__init__(parent)

        self.profiles = profiles

        layout = QVBoxLayout(self)

        label = QLabel("Applications")
        layout.addWidget(label)

        # TODO: Check if can be implemented, I did not find a way to
        # make the items in the list clickable
        # list_model = QStandardItemModel(0, 1)

        for index, profile in enumerate(profiles):
            # list_model.appendRow(QStandardItem(profile.name))
            item = ListItem(profile.name, self)
            item.edit_button.clicked.connect(lambda _c, i=index: self.edit_clicked(i))
            layout.addWidget(item)

        # list_view = QListView()
        # list_view.setModel(list_model)
        # layout.addWidget(list_view)

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
