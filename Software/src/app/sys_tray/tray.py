import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon
from PySide6.QtCore import Slot


class Tray(QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, parent=None):
        super(Tray, self).__init__(parent)

        self.menu = QMenu()
        self.action = QAction("A menu item")
        self.menu.addAction(self.action)

        self.quit = QAction("Quit")
        self.menu.addAction(self.quit)

        self.setIcon(QIcon("src/assets/icon.ico"))
        self.setContextMenu(self.menu)
        self.setToolTip("Shokey")
