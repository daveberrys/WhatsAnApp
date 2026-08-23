<!-- action go -->

<div align="center">
    <img src="assets/WhatsAnApp.png" width=250>
    <h1>WhatsAnApp</h1>
    <p>WhatsApp, if it were more comfortable to keep in your computer.</p>
</div>

<div align="center">
    <a href="https://github.com/daveberrys/WhatsAnApp?tab=readme-ov-file#required-dependencies-to-open-the-app">Required dependencies to open the app</a> <br>
    <a href="https://github.com/daveberrys/WhatsAnApp?tab=readme-ov-file#required-dependencies-to-open-the-app">How to build the app</a> <br>
    <a href="https://github.com/daveberrys/WhatsAnApp?tab=readme-ov-file#download-for">Download the app</a> <br>
    <a href="https://github.com/daveberrys/WhatsAnApp?tab=readme-ov-file#heres-how-the-app-works">How the app works</a>
</div>

> [!CAUTION]
> Use this at your own risk. We are not responsible if your account was deleted, even if it's a native-app feel.

> [!NOTE]
> We've gone ahead and done a 180 and made a native app instead. I (Daveberry) found out that it uses less RAM than native windows, so why not make this an alternative to the native Whatsapp app? And we're completely removing the UI change, but still keeping loading themes.

> [!WARNING]
> Linux version of this app is currently a bit stupid. At 140+ mb compiled. We'll try to find a fix, don't worry fellow Linux users.

> [!NOTE]
> This app development is paused.

---

WhatsAnApp (Also known as What's an app?) is a native-app feel and less usage of your memory.

The full native version of Whatsapp is too bloated, taking about 1-2+ **GB** of memory usage due to electron. WhatsAnApp only takes about 50-100 **MB** using PyWebView and Python. We could probably achieve less by using Rust, but Python is good enough.

---

### Here's how the app works:
```text
Python Project
  v
Libraries:
- PyWebView
- PyInstaller
  v
PyWebView makes a new window, and opens the whatsapp website.
Python handles reading files, creating new files, editing, and such.
PyInstaller compiles the project into one file.
  v
Benefits?
Low chance of getting temp/perm ban from Meta
Easily be able to make your own theme with CSS/JS
Better UI instead of Meta's UI.
Native App for Linux (And a Better UI for Win+Mac)
Open source, free forever.
```

---

If you want us to add modification (message logs, read receips and such) to WhatsApp web, we're not doing it. We're not risking a cease and desist letter from Meta, the parent company of WhatsApp.

> [!NOTE]
> Please note that if you want modification, do it yourself or ask someone to do it. Not the official devs of `WhatsAnApp`. If you do make modifications, be VERY aware that you have a high chance of getting a cease and desist from Meta.

---

## Download for:
- [Windows](https://nightly.link/daveberrys/WhatsAnApp/workflows/building/main/WhatsAnApp-Windows.zip)
- [macOS](https://nightly.link/daveberrys/WhatsAnApp/workflows/building/main/WhatsAnApp-macOS.zip)
- [Linux](https://nightly.link/daveberrys/WhatsAnApp/workflows/building/main/WhatsAnApp-Linux.zip)

---

## Required Dependencies (to open the app):
If you're using Linux Ubuntu, then run this command below:
```bash
sudo apt install xvfb libxcb-cursor0 libxcb-xinerama0 libxkbcommon-x11-0
```
I dunno about other distros through. Good luck finding it because I use DistroBox with Ubuntu. (Confirmed by [@Daveberrys](https://codedave.pages.dev/))

If you're using Windows, all you need is WebView2 which is built in. If you somehow don't have WebView2, the link is here: [Download WebView2 here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH#download) (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/) & [@Daveberrys](https://zcodedave.pages.dev/))

If you're using macOS, you don't need any libraries to open the app. Just open the app and it'll launch with no problems at all. (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))

## Building WhatsAnApp:
### In Linux Ubuntu, here are the steps: (Confirmed by [@Daveberrys](codedave.pages.dev/))
```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv xvfb libxcb-cursor0 libxcb-xinerama0 libxkbcommon-x11-0
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
python3 -m venv venv
venv/bin/pip install -r python/requirements-linux.txt
venv/bin/pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By Daveberry)</summary>
    <img src="readme/Linux (Daveberry).png"/>
</details>

### In Windows, here are the steps: (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))
> [!IMPORTANT]
> Since the module Pythonnet fails to build on Python 3.14.x on Windows, you must downgrade to 3.13.x before setting up the environment.

In windows, you have two options to install it.

#### Option 1:
```powershell
# Install pyenv-win to manage Python versions
Invoke-WebRequest -UseBasicParsing `
  -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" `
  -OutFile "./install-pyenv-win.ps1"
& "./install-pyenv-win.ps1"

# Close PowerShell after installation, Open cmd

# Install and activate Python 3.13 (.11 is latest version As of Jan 10, 2026)
pyenv install 3.13.11
pyenv global 3.13.11
```

#### Option 2:
```powershell
# Assuming you have winget installed (which is by-default installed in windows.)
winget install python3.13

# Then, you can finally just initialize python's virtual environment in 3.13 easily.
python -3.13 -m venv venv
```

#### Then finally, the final commands.
```powershell
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
python3 -m venv venv
venv\Scripts\pip install -r python\requirements.txt
venv\Scripts\pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By TK50P)</summary>
     <img src="readme/Windows (TK50P).png"/> 
</details>

### In macOS, here are the steps: (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))
```bash
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
python3 -m venv venv
venv/bin/pip install -r python/requirements.txt
venv/bin/pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By TK50P)</summary>
    <img src="readme/macOS (TK50P).png"/>
</details>
