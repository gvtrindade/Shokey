import json
import sys
import threading

from app.main_window import MainWindow
from app.sys_tray.tray import Tray
from PySide6.QtWidgets import QApplication
from util.communication import Communication

comm = Communication()
app = None
main_window = None
tray = None


def main():
    print("Starting Shokey")
    tray.show()
    tray.action.triggered.connect(main_window.show)
    tray.quit.triggered.connect(app.quit)
    main_window.show()

    threading.Thread(target=comm_loop).start()

    sys.exit(app.exec())


def comm_loop():
    comm.search_port()

    print("Found port")
    used_port = comm.find_used_port()
    comm.establish_connection(used_port)
    comm.send_data(json.dumps({"app": "shortcut", "action": "load", "data": ""}))
    main_window.show_shokey()

    print("Starting communication")
    while True:
        try:
            crude_data = comm.read_data()
            data = comm.actions.parse_data(crude_data)
            if isinstance(data, str):
                comm.shortcuts.execute_shortcut(data)
            else:
                comm.actions.execute_action(data)
        except Exception as e:
            print(e)
            main_window.hide_shokey()
            # TODO restablishing the loop should be done better
            comm_loop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    main_window = MainWindow()
    tray = Tray()

    main()
