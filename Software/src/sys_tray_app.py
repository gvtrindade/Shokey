import os
import sys

from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import pyqtSignal


class SystemTrayIcon(QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("Shokey")
        self.windows = []

        menu = QMenu(parent)
        open_app = menu.addAction("Open Notepad")
        open_app.triggered.connect(self.open_notepad)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            self.open_notepad()
        # if reason == self.Trigger:
        #     self.open_notepad()

    def open_notepad(self):
        """
        this function will open application
        :return:
        """
        print("Creating window")
        w = Window()
        self.windows.append(w)
        w.show()

        w.closed.connect(lambda: self.remove_window(w))

    def remove_window(self, window):
        """
        Remove the closed window from the windows list
        """
        self.windows.remove(window)
        print(self.windows)


class Window(QWidget):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Shokey - Edit shortcuts")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def closeEvent(self, event):
        self.closed.emit()
        # event.accept()
