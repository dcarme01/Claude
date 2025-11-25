#!/bin/bash
#
# Kalshi Bet Analyzer - Debug Launcher
# Runs with full error output for troubleshooting
#

echo "🎰 Kalshi Bet Analyzer - Debug Mode"
echo "===================================="
echo ""

# Change to script directory
cd "$(dirname "$0")"

echo "📂 Current directory: $(pwd)"
echo ""

# Check Python
echo "🐍 Python version:"
python3 --version
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv || {
        echo "❌ Failed to create virtual environment"
        exit 1
    }
fi

# Activate venv
echo "🔌 Activating virtual environment..."
source venv/bin/activate || {
    echo "❌ Failed to activate virtual environment"
    exit 1
}

# Check pip
echo "📦 Pip version:"
pip --version
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt || {
    echo "❌ Failed to install dependencies"
    exit 1
}
echo ""

# Check .env
if [ ! -f ".env" ]; then
    echo "⚠️  WARNING: No .env file found"
    echo "Creating .env from example..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo ""
        echo "📝 Please edit .env and add your Kalshi credentials:"
        echo "   open -e .env"
        echo ""
        echo "Press Ctrl+C to exit and configure, or"
        read -p "Press Enter to continue anyway (will use demo data)..."
    fi
fi

echo ""
echo "🔍 Running system check..."
python3 test_setup.py
echo ""

echo "🚀 Launching app with full error output..."
echo "   (If the app crashes, you'll see the error below)"
echo ""

# Run with full error output
python3 mac_app.py 2>&1

echo ""
echo "App closed."
