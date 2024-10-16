import sys
import time
import threading

from PyQt5 import QtWidgets, QtGui

from communication import establish_connection, send_serial_msg
from key_parse_functions import communication_handler
from search_ports import find_used_port
from shortcuts import set_shortcuts
from sys_tray_app import SystemTrayIcon

COMM_RETRY_TIMEOUT = 0.8


def update_communication():
    used_port = find_used_port()
    serialcomm = establish_connection(used_port)
    send_serial_msg(serialcomm, "I")

    shortcuts = {}
    set_shortcuts(shortcuts)

    while True:
        try:
            communication_handler(serialcomm, shortcuts)

        except Exception as e:
            print(e)
            find_used_port()
            if find_used_port():
                update_communication()
            time.sleep(COMM_RETRY_TIMEOUT)


def comm_loop():
    while not find_used_port():
        find_used_port()
        time.sleep(COMM_RETRY_TIMEOUT)

    update_communication()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()

    # threading.Thread(target=comm_loop).start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
