<div align="center">
    <img src="assets/WhatsAnApp.png" width=80>
    <h1>WhatsAnApp</h1>
    <p>WhatsApp, with a sleek and modified UI.</p>
</div>

> [!CAUTION]
> Use this at your own risk. We are not responsible if your account was deleted, even if it's a UI Modification.

---

WhatsAnApp (Also known as What's an app?) is a UI modification to WhatsApp's Shitty UI and Removing unwanted features.

WhatsAnApp is a UI modification. Not a full modification for WhatsApp. We're not trying to get our ass sued by Meta.

---

WhatsAnApp is a python project based app using Flask and PyWebView. Making it easier yet having more control without fucking around and fetching their API and getting our ass sued.

We believe that we deserve a Better UI than whatever the fuck they made. Going all in with the UI change.

---

If you want us to add modification (message logs, read receips and such) to WhatsApp web, we're not doing it. We're not risking a cease and desist letter from Meta, the parent company of WhatsApp.

> [!NOTE]
> Please note that if you want modification, do it yourself or ask someone to do it. Not the official devs of `WhatsAnApp`. If you do make modifications, be VERY aware that you have a high chance of getting a cease and desist from Meta.

---

Available in:
- Linux
- Windows
- MacOS 

---

## Required Dependencies (to open the app):
If you're using Linux Ubuntu, then run this command below:
```bash
sudo apt install xvfb libxcb-cursor0 libxcb-xinerama0 libxkbcommon-x11-0
```
I dunno about other distros through. Good luck finding it because I use DistroBox with Ubuntu. (Confirmed by [@Daveberrys](https://daveberry.netlify.app/))

If you're using Windows, all you need is WebView2 which is built in. If you somehow don't have WebView2, the link is here: [Download WebView2 here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH#download) (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/) & [@Daveberrys](https://daveberry.netlify.app/))

If you're using MacOS, you don't need any libraries to open the app. Just open the app and it'll launch with no problems at all. (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))

## Building WhatsAnApp:
In Linux Ubuntu, here are the steps: (Confirmed by [@Daveberrys](https://daveberry.netlify.app/))
```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv xvfb libxcb-cursor0 libxcb-xinerama0 libxkbcommon-x11-0
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rm -rf .git
python3 -m venv venv
venv/bin/pip install -r python/requirements-linux.txt
venv/bin/pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By Daveberry)</summary>
    <img src="readme/Linux (Daveberry).png"/>
</details>

In Windows, here are the steps: (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))
> [!IMPORTANT]
> Since the module Pythonnet fails to build on Python 3.14.x on Windows, you must downgrade to 3.13.x before setting up the environment.

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

git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rd /s /q .git
python3 -m venv venv
venv\Scripts\pip install -r python/requirements.txt
venv\Scripts\pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By TK50P)</summary>
     <img src="readme/Windows (TK50P).png"/> 
</details>

In MacOS, here are the steps: (Confirmed by [@TK50P](https://www.tk50piscool.kro.kr/))
```bash
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rm -rf .git
python3 -m venv venv
venv/bin/pip install -r python/requirements.txt
venv/bin/pyinstaller WhatsAnApp.spec
```
<details>
    <summary>Screenshot Preview (By TK50P)</summary>
    <img src="readme/MacOS (TK50P).png"/>
</details>