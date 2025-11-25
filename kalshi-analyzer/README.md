# Kalshi Bet Analyzer

A powerful platform that analyzes Kalshi prediction markets with **live, real-time data** and identifies potentially profitable bets.

## 🚀 Choose Your Platform

### 🍎 macOS Desktop App (New! - Recommended for Mac Users)

**Native Mac application with live market analysis and auto-refresh!**

Features:
- 🔴 **Live market data** with configurable auto-refresh (30s-5min intervals)
- 🎨 **Beautiful native Mac interface** using SF Pro fonts
- 📊 **Real-time updates** - never miss an opportunity
- 🔍 **Detailed market analysis** with double-click details
- 📱 **Menu bar app** for quick access
- ⚡ **Fast & responsive** - multi-threaded design

**Quick Start:**
```bash
cd kalshi-analyzer
./run-mac-app.sh
```

👉 **[Full macOS Setup Guide (MAC_SETUP.md)](MAC_SETUP.md)**

---

## 📱 iPhone-Only Deployment (No Computer Needed!)

**Want to use this entirely from your iPhone?** Check out the full guide:

👉 **[iPhone Deployment Guide (DEPLOY.md)](DEPLOY.md)**

Deploy to the cloud in 5 minutes using:
- **Render.com** (Recommended - 100% free)
- **Railway.app** (Free tier)
- **Replit** (Easy but may require payment)

Access your analyzer from anywhere, 24/7, with no computer required!

---

## 🌐 Web Interface (Cross-Platform)

Run the web interface on any device with a browser.

**Quick Start:**
```bash
cd kalshi-analyzer
./start-mobile.sh
```

Then visit `http://localhost:5000` or access from your phone on the same WiFi network.

---

## 📊 Platform Comparison

| Feature | macOS App | Web Interface | iPhone Cloud |
|---------|-----------|---------------|--------------|
| **Live Auto-Refresh** | ✅ Built-in | ❌ Manual | ❌ Manual |
| **Native Experience** | ✅ Native Mac | 🌐 Browser | 📱 Mobile Web |
| **Setup Time** | 2 minutes | 2 minutes | 5 minutes |
| **Access Anywhere** | ❌ Mac only | ✅ Local network | ✅ Anywhere |
| **Best For** | Mac power users | Multi-device | Mobile-only |

---

## 💻 Local Setup (If You Have a Computer)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your Kalshi credentials:
```bash
cp .env.example .env
# Edit .env and add your Kalshi credentials
```

3. Run the analyzer:
```bash
python analyzer.py
```

4. Or run the web interface:
```bash
python app.py
```

Then visit http://localhost:5000

## 📱 Access from iPhone

The web interface is fully mobile-optimized! To access from your iPhone:

### Quick Start (Recommended)

```bash
./start-mobile.sh
```

This script will automatically:
- Detect your computer's IP address
- Show you the URL to visit on your iPhone
- Start the web server

### Manual Setup

1. **Make sure your iPhone and computer are on the same WiFi network**

2. **Find your computer's local IP address:**
   - **Mac**:
     ```bash
     ipconfig getifaddr en0
     ```
   - **Linux**:
     ```bash
     hostname -I | awk '{print $1}'
     ```
   - **Windows**:
     ```bash
     ipconfig
     ```
     (Look for IPv4 Address)

3. **Start the server:**
   ```bash
   python app.py
   ```

4. **On your iPhone, open Safari and visit:**
   ```
   http://YOUR-IP-ADDRESS:5000
   ```

   For example, if your IP is 192.168.1.100:
   ```
   http://192.168.1.100:5000
   ```

5. **Add to Home Screen** (optional):
   - Tap the Share button in Safari
   - Select "Add to Home Screen"
   - Now you have a quick-access app icon!

The interface automatically adapts to your iPhone screen size with:
- Touch-friendly buttons
- Optimized layout for mobile
- Easy scrolling through markets
- Full functionality on the go

## How It Works

The analyzer evaluates markets based on:
- **Volume & Liquidity**: Higher volume = more reliable prices
- **Spread Analysis**: Tight spreads indicate market efficiency
- **Probability Mispricing**: Identifies markets where prices don't match fair value
- **Time to Close**: Considers when the market closes
- **Market Momentum**: Analyzes recent price movements

## Features

- Fetches live Kalshi markets
- Analyzes each market for value
- Scores opportunities from 1-10
- Provides reasoning for each recommendation
- Web interface for easy viewing

## 🎯 Quick Launch Reference

### macOS Users
```bash
# Full desktop app with live updates
./run-mac-app.sh

# Menu bar app for quick access
./run-menubar.sh

# Web interface
./start-mobile.sh
```

### Command Line
```bash
# One-time analysis
python analyzer.py

# Web server
python app.py
```

## 🔧 Advanced: Creating a Standalone Mac App

Want a double-clickable Mac application?

```bash
pip install py2app
python setup.py py2app
```

Your app will be in `dist/KalshiBetAnalyzer.app` - move it to Applications!

## Disclaimer

This tool is for educational purposes. Past performance doesn't guarantee future results. Always do your own research before placing bets.
