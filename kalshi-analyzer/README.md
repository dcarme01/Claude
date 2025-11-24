# Kalshi Bet Analyzer

An app that analyzes Kalshi prediction markets and identifies potentially profitable bets.

## Setup

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

## Disclaimer

This tool is for educational purposes. Past performance doesn't guarantee future results. Always do your own research before placing bets.
