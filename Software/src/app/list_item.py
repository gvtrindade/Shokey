from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget


class ListItem(QWidget):
    def __init__(self, label, profile, parent=None):
        super(ListItem, self).__init__(parent)
        self.profile = profile

        self.label = QLabel(label)
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.layout = QHBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)
        self.setLayout(self.layout)
