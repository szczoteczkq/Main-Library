@echo off
python -m pip install Pillow requests

echo.
echo Starting screensaver.py...
cd /d "%USERPROFILE%\Downloads"
python screensaver.py

pause