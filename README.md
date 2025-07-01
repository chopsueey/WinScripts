## Info

This app uses the Hyper-V-Automation repository: https://github.com/fdcastel/Hyper-V-Automation

## Install packages

pip install -r requirements.txt

### Create an onefile .exe (automatically creates files in current user temp folder)

pyinstaller --noconfirm --onefile --windowed --icon=".\favicon.ico" --add-data ".\favicon.ico;." --add-data "scripts;scripts" --add-data "icons;icons" .\main.py

### Create a directory with .exe and dependencies

pyinstaller --noconfirm --onedir --windowed --icon=".\favicon.ico" --add-data ".\favicon.ico;." --add-data "scripts;scripts" --add-data "icons;icons" .\main.py