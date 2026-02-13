import os
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

import src.back.system.settings as settings
import src.back.utils.print as print
from src.back.system.pyqt6 import SystemTrayIcon, WhatsAppWindow

def startUp(debugMode=False):
    settings.checkIfExist()
    print.success("PyQt6 and QtWebView2 is starting! Please wait...")

    if debugMode:
        print.debug("Debug mode enabled for WhatsAnApp")

    # Create Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("WhatsAnApp")
    app.setQuitOnLastWindowClosed(False)

    # Get icon path
    projectRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if sys.platform == "win32":
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.ico")
    else:
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.png")

    # Create main window
    window = WhatsAppWindow(iconPath, debugMode)

    # Create system tray
    if os.path.exists(iconPath):
        trayIcon = SystemTrayIcon(QIcon(iconPath), window)
    else:
        print.warning(f"Icon not found at {iconPath}")
        trayIcon = SystemTrayIcon(QIcon(), window)

    trayIcon.show()
    window.show()

    # Start event loop
    print.success("WhatsAnApp is ready!")
    sys.exit(app.exec())
