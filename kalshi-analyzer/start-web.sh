#!/bin/bash
#
# Start the Kalshi Bet Analyzer Web App
#

cd "$(dirname "$0")"

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup.sh first"
    exit 1
fi

source venv/bin/activate

# Start the app
echo "🎰 Starting Kalshi Bet Analyzer..."
echo ""
echo "🌐 Open your browser to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 app.py
