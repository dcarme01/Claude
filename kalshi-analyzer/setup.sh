#!/bin/bash
#
# Simple Setup Script for Kalshi Bet Analyzer
# This will get everything working in one go
#

echo "🎰 Kalshi Bet Analyzer - Complete Setup"
echo "========================================"
echo ""

# Go to the right directory
cd "$(dirname "$0")"
echo "📂 Working directory: $(pwd)"
echo ""

# Step 1: Check Python
echo "1️⃣  Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install it from https://www.python.org/"
    exit 1
fi
python3 --version
echo ""

# Step 2: Create virtual environment
echo "2️⃣  Setting up virtual environment..."
if [ -d "venv" ]; then
    echo "   Virtual environment already exists"
else
    python3 -m venv venv
    echo "   ✅ Created virtual environment"
fi
echo ""

# Step 3: Activate and install
echo "3️⃣  Installing dependencies..."
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo "   ✅ All dependencies installed"
echo ""

# Step 4: Configure .env
echo "4️⃣  Configuring credentials..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "   ✅ Created .env file"
    echo ""
    echo "   ⚠️  IMPORTANT: You need to edit .env with your Kalshi credentials!"
    echo ""
    echo "   Opening .env file now..."
    sleep 2
    open -e .env 2>/dev/null || nano .env
    echo ""
    echo "   Please edit the file with:"
    echo "   - Your KALSHI_EMAIL"
    echo "   - Your KALSHI_PASSWORD"
    echo "   - Keep KALSHI_DEMO_MODE=true for testing"
    echo ""
    read -p "   Press Enter after you've saved your credentials..."
else
    echo "   ✅ .env file already exists"

    # Check if configured
    if grep -q "your_email@example.com" .env; then
        echo "   ⚠️  WARNING: .env still has example values!"
        echo ""
        read -p "   Do you want to edit it now? (y/n) " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            open -e .env 2>/dev/null || nano .env
            read -p "   Press Enter after you've saved your credentials..."
        fi
    else
        echo "   ✅ Credentials configured"
    fi
fi
echo ""

# Step 5: Test everything
echo "5️⃣  Testing configuration..."
python3 test_setup.py
echo ""

# Step 6: Ready!
echo "========================================"
echo "✅ Setup Complete!"
echo "========================================"
echo ""
echo "🚀 To start the web app:"
echo "   ./start-web.sh"
echo ""
echo "   Then open: http://localhost:5000"
echo ""
echo "Happy analyzing! 🎰"
