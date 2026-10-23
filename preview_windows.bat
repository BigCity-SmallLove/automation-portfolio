@echo off
cd /d "%~dp0"
python -m http.server 8080 --directory site --bind 127.0.0.1
pause
