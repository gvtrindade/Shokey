import os
import sys
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 


class SystemTrayIcon(QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip('Shokey')
        menu = QMenu(parent)
        open_app = menu.addAction("Open Notepad")
        open_app.triggered.connect(self.open_notepad)

        open_cal = menu.addAction("Open Calculator")
        open_cal.triggered.connect(self.open_calc)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        if reason == self.DoubleClick:
            self.open_notepad()


    def open_notepad(self):
        sys.exit()

    def open_calc(self):
        os.system('calc')


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    tray_icon = SystemTrayIcon(QIcon("icon.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

while True:
    me = "dumb"