#!/bin/bash

echo "🏫 School Inspection Form - Startup Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python 3 found"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "✓ All dependencies installed!"
echo ""
echo "🌐 Starting Flask server..."
echo "📍 Open your browser and go to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
