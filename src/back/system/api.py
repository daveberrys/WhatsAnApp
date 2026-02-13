import sys

from plyer import notification

if sys.platform == "win32":
    import win32con
    import win32gui
elif sys.platform == "darwin":
    try:
        from AppKit import NSApp, NSApplication, NSRunningApplication
        from Foundation import NSBundle
    except ImportError:
        pass
elif sys.platform == "linux":
    import os

class WhatsAnAppAPI:
    def __init__(self, appIcon=None):
        self.lastTitle = ""
        self.lastBody = ""
        self.appIcon = appIcon

    def sendNotif(self, title, body):
        try:
            notification.notify(
                title=title,
                message=body,
                timeout=5,
                app_name="WhatsAnApp",
                app_icon=self.appIcon,
            )
            self.lastTitle = title
            self.lastBody = body
            return "Notification sent"
        except Exception as e:
            return f"Error: {e}"

    def focusWindow(self):
        system = sys.platform
        try:
            if system == "win32":
                hwnd = win32gui.FindWindow(None, "WhatsAnApp")
                if hwnd:
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.SetForegroundWindow(hwnd)
            elif system == "darwin":
                NSRunningApplication.currentApplication().activateWithOptions_(1 << 1)
            elif system == "linux":
                os.system("wmctrl -a 'WhatsAnApp'")
        except Exception as e:
            print(f"Could not focus window: {e}")
