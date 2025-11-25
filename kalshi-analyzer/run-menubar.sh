#!/bin/bash
#
# Kalshi Bet Analyzer - Menu Bar App Launcher
# Launches the menu bar version for quick access
#

echo "🎰 Starting Kalshi Menu Bar App..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies quietly
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "Created .env from example. Please configure your credentials."
    fi
fi

# Launch the menu bar app
python3 menubar_app.py
