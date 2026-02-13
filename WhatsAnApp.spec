# -*- mode: python ; coding: utf-8 -*-
import sys
import os
import qtwebview2
from PyInstaller.utils.hooks import collect_all

# Collect metadata/binaries for Webview
datas_wv, binaries_wv, hiddenimports_wv = collect_all('webview')

qtWebview2Path = os.path.dirname(qtwebview2.__file__)
qtWebview2LibData = (os.path.join(qtWebview2Path, 'lib'), 'lib')

if sys.platform == "win32":
    icon_file = "assets/WhatsAnApp.ico"
else:
    icon_file = "assets/WhatsAnApp.png"

hidimports = [
    'pywebview',
    'flask',
    'qtpy',
    'PyQt6',
    'PyQt6-WebEngine',
]

if sys.platform == "win32":
    hidimports.extend([
        'qtwebview2',
        'pywin32'
    ])
elif sys.platform == "darwin":
    hidimports.extend([
        'pyobjc'
    ])

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries_wv,
    datas=[('assets', 'assets'), qtWebview2LibData] + datas_wv,
    hiddenimports= hidimports + hiddenimports_wv,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='WhatsAnApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file
)
