@echo off
echo 🏫 School Inspection Form - Startup Script
echo ==========================================
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python found

if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

echo 🚀 Activating virtual environment...
call venv\Scripts\activate.bat

echo 📥 Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ✓ All dependencies installed!
echo.
echo 🌐 Starting Flask server...
echo 📍 Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
