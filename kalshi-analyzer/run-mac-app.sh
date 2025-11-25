#!/bin/bash
#
# Kalshi Bet Analyzer - macOS Launcher
# Quick launcher for the Mac desktop application
#

echo "🎰 Kalshi Bet Analyzer for macOS"
echo "================================="
echo ""

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

# Install/upgrade dependencies
echo "📦 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found."
    if [ -f ".env.example" ]; then
        echo "Creating .env from .env.example..."
        cp .env.example .env
        echo ""
        echo "📝 Please edit .env and add your Kalshi credentials:"
        echo "   open -t .env"
        echo ""
        read -p "Press Enter after configuring your credentials..."
    fi
fi

echo ""
echo "🚀 Launching Kalshi Bet Analyzer..."
echo ""

# Launch the Mac app
python3 mac_app.py
