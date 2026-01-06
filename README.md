<div align="center">
    <img src="assets/WhatsAnApp.png">
    <h1>WhatsAnApp</h1>
    <p>WhatsApp, with a sleek and modified UI.</p>
</div>

---
WhatsAnApp (Also known as What's an app?) is a UI modification to WhatsApp's Shitty UI and Removing unwanted features.

WhatsAnApp is a UI modification. Not a full modification for WhatsApp. We're not trying to get our ass sued by Meta.

---

WhatsAnApp is a python project based app using Flask and PyWebView. Making it easier yet having more control without fucking around and fetching their API and getting our ass sued.

We believe that we deserve a Better UI than whatever the fuck they made. Going all in with the UI change.

---

If you want us to add modification (message logs, read receips and such) to WhatsApp web, we're not doing it.

We're not risking a cease and desist letter from Meta, the parent company of WhatsApp.

Please note that if you want modification, do it yourself or ask someone to do it. Not the official devs of `WhatsAnApp`. If you do make modifications, be VERY aware that you have a high chance of getting a cease and desist from Meta.

---

Available in:
- Linux
- Windows
- MacOS (probably)

---

## Required Dependencies (to open the app):
If you're using Linux Ubuntu, then run this command below:
```bash
sudo apt install libgirepository-2.0-dev gir1.2-gtk-3.0 gir1.2-webkit2-4.1 libcanberra-gtk-module libcanberra-gtk3-module
```
I dunno about other distros through. Good luck finding it because I use DistroBox with Ubuntu.

If you're using Windows, all you need is WebView2 which is built in. If you somehow don't have WebView2, the link is here: [Download WebView2 here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH#download)

If you're using MacOS, I dunno. If it doesn't launch, you're on your own because I don't use MacOS. Feel free to help out with MacOS.

## Building WhatsAnApp:
In Linux Ubuntu, here are the steps:
```bash
sudo apt update && yes | sudo apt install python3 python3-pip python3-venv libgirepository-2.0-dev gir1.2-gtk-3.0 gir1.2-webkit2-4.1 cmake libcanberra-gtk-module libcanberra-gtk3-module xvfb pkg-config python3-cairo libcairo2-dev
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rm -rf .git
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python main.py
```

In Windows, here are the steps:
```powershell
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rm -rf .git
python3 -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\python main.py
```

In MacOS, here are the steps: (NOT TESTED, PLEASE DO AN ISSUE IF YOU USE THIS SCRIPT IF IT'S WORKING OR NOT.)
```bash
git clone https://github.com/daveberrys/WhatsAnApp/
cd WhatsAnApp
rm -rf .git
python3 -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\python main.py
```