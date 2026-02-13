import os
import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenu, QSystemTrayIcon

import src.back.system.settings as settings
import src.back.utils.print as print
from src.back.system.api import WhatsAnAppAPI

# --- CROSS-PLATFORM ENGINE SELECTION ---
IS_WINDOWS = sys.platform == "win32"

if IS_WINDOWS:
    # Windows: Use WebView2 for full video codec support
    from qtwebview2 import QtWebView2Widget
    try:
        from Microsoft.Web.WebView2.Core import CoreWebView2PermissionState
    except ImportError:
        CoreWebView2PermissionState = None
    BaseWindow = QtWebView2Widget
else:
    # Linux/macOS: Use standard QWebEngine
    from PyQt6.QtWebEngineCore import (
        QWebEngineProfile,
        QWebEnginePage,
        QWebEngineSettings,
        QWebEngineNotification
    )
    from PyQt6.QtWebEngineWidgets import QWebEngineView
    BaseWindow = QWebEngineView


class WhatsAppWindow(BaseWindow):
    def __init__(self, iconPath, debugMode=False):
        self.debugMode = debugMode
        self.wvapi = WhatsAnAppAPI()
        self.iconPath = iconPath
        
        # Consistent User Agent across all platforms
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

        if IS_WINDOWS:
            self._init_windows(debugMode)
        else:
            self._init_unix(debugMode)

        self._setupWindow()

    def _init_windows(self, debugMode):
        """Setup for Windows using WebView2"""
        storagePath = os.path.join(settings.fullAppConfig, "Edge Storage")
        jsApis = {"send_notification": self._handle_win_notification}
        
        # Initialize the QtWebView2Widget
        super().__init__(
            url="https://web.whatsapp.com/",
            user_agent=self.userAgent,
            user_data_folder=storagePath,
            debug=debugMode,
            context_menus=debugMode,
            js_apis=jsApis,
            init_settings_hook=self._configure_view2
        )

    def _init_unix(self, debugMode):
        """Setup for Linux/macOS using QWebEngine"""
        super().__init__()
        storagePath = os.path.join(settings.fullAppConfig, "Chromium Storage")
        
        profile = QWebEngineProfile("WhatsAnApp", self)
        profile.setPersistentStoragePath(storagePath)
        profile.setCachePath(os.path.join(storagePath, "cache"))
        profile.setHttpUserAgent(self.userAgent)
        profile.setNotificationPresenter(self._handle_unix_notification)
        
        page = QWebEnginePage(profile, self)
        self.setPage(page)
        self.setUrl(QUrl("https://web.whatsapp.com/"))
        
        webSettings = self.settings()
        webSettings.setAttribute(QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False)
        webSettings.setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        
        if self.debugMode:
             webSettings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)

    def _handle_win_notification(self, title, body):
        """Called from JS bridge on Windows"""
        if self.debugMode:
            print.debug(f"Notification received (Win): {title} - {body}")
        self.wvapi.sendNotif(title, body)

    def _handle_unix_notification(self, notification):
        """Called from QWebEngine on Linux/macOS"""
        title = notification.title()
        body = notification.message()
        if self.debugMode:
            print.debug(f"Notification received (Unix): {title} - {body}")
        self.wvapi.sendNotif(title, body)
        notification.show()

    def _configure_view2(self, core):
        """Configure Windows-specific permission auto-grants and notification shim"""
        core.PermissionRequested += self._handle_win_permissions
        
        # Inject Notification shim to bridge WhatsApp notifications to Python
        shim_script = """
        (function() {
            const OriginalNotification = window.Notification;
            function CustomNotification(title, options) {
                const body = (options && options.body) ? options.body : "";
                window.qtwebview2.api.send_notification(title, body);
                return {
                    close: function() {},
                    onclick: null,
                    onclose: null,
                    onerror: null,
                    onshow: null
                };
            }
            CustomNotification.permission = "granted";
            CustomNotification.requestPermission = function(callback) {
                if (callback) callback("granted");
                return Promise.resolve("granted");
            };
            window.Notification = CustomNotification;
            console.log("WhatsAnApp: Notification shim injected");
        })();
        """
        core.AddScriptToExecuteOnDocumentCreatedAsync(shim_script)

    def _handle_win_permissions(self, sender, args):
        """Auto-grant permissions on Windows WebView2"""
        if CoreWebView2PermissionState:
            # Grant Notifications or Camera/Mic if requested
            kind = str(args.PermissionKind).lower()
            if "notifications" in kind or "microphone" in kind or "camera" in kind:
                args.State = CoreWebView2PermissionState.Allow
                args.Handled = True
                if self.debugMode:
                    print.debug(f"Auto-granted permission: {kind}")

    def _setupWindow(self):
        """Configure window properties"""
        self.setWindowTitle("WhatsAnApp")
        self.resize(1280, 720)

        if os.path.exists(self.iconPath):
            self.setWindowIcon(QIcon(self.iconPath))
            print.debug(f"Using window icon at: {self.iconPath}")


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, window):
        super().__init__(icon)
        self.window = window

        self._createMenu()
        self.setToolTip("WhatsAnApp")
        self.activated.connect(self._onActivated)

        print.success("System tray icon created!")

    def _createMenu(self):
        menu = QMenu()

        showAction = QAction("Show WhatsAnApp", menu)
        showAction.triggered.connect(self._showWindow)
        menu.addAction(showAction)

        hideAction = QAction("Hide to Tray", menu)
        hideAction.triggered.connect(self._hideWindow)
        menu.addAction(hideAction)

        menu.addSeparator()

        quitAction = QAction("Quit", menu)
        quitAction.triggered.connect(QApplication.quit)
        menu.addAction(quitAction)

        self.setContextMenu(menu)

    def _onActivated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.window.isVisible():
                self._hideWindow()
            else:
                self._showWindow()

    def _showWindow(self):
        self.window.show()
        self.window.activateWindow()
        self.window.raise_()

    def _hideWindow(self):
        self.window.hide()

