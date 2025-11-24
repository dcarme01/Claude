#!/bin/bash
# Quick start script for mobile access

echo "🎰 Kalshi Bet Analyzer - Mobile Setup"
echo "======================================"
echo ""

# Detect OS and get IP
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    IP=$(ipconfig getifaddr en0 2>/dev/null)
    if [ -z "$IP" ]; then
        IP=$(ipconfig getifaddr en1 2>/dev/null)
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    IP=$(hostname -I | awk '{print $1}')
else
    # Try a generic approach
    IP=$(hostname -I 2>/dev/null | awk '{print $1}')
fi

if [ -z "$IP" ]; then
    echo "⚠️  Could not detect IP address automatically"
    echo ""
    echo "Please find your IP address manually:"
    echo "  Mac:     ipconfig getifaddr en0"
    echo "  Linux:   hostname -I"
    echo "  Windows: ipconfig"
    echo ""
else
    echo "✅ Your computer's IP address: $IP"
    echo ""
    echo "📱 On your iPhone, open Safari and visit:"
    echo ""
    echo "   http://$IP:5000"
    echo ""
    echo "======================================"
    echo ""
fi

echo "🚀 Starting web server..."
echo ""

# Start the Flask app
python3 app.py
