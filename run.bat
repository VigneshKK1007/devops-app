@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "PYTHON=%PROJECT_DIR%.venv\Scripts\python.exe"

if not exist "%PYTHON%" (
    echo Could not find the project Python at:
    echo %PYTHON%
    echo.
    echo Create a virtual environment and install requirements first:
    echo python -m venv .venv
    echo .venv\Scripts\python.exe -m pip install -r requirements.txt
    exit /b 1
)

"%PYTHON%" -m flask --app app run --debug
