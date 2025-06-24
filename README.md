### Create an .exe

pip install pyinstaller

pyinstaller --onefile --noconsole --icon=".\favicon.ico" --add-data ".\favicon.ico;." .\main.py