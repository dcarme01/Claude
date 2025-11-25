# 🍎 Kalshi Bet Analyzer - macOS Desktop Application

A native macOS desktop application for analyzing Kalshi prediction markets with **live, real-time data updates**.

## ✨ Features

- **🔴 Live Market Analysis**: Real-time bet analysis with auto-refresh capabilities
- **📊 Native macOS Interface**: Beautiful, native Mac design using SF Pro fonts
- **⚡ Auto-Refresh**: Configure automatic market updates (30s, 60s, 2min, 5min intervals)
- **🎯 Top Opportunities View**: Quickly see the best betting opportunities
- **📈 All Markets Table**: Browse all analyzed markets in a sortable table
- **🔍 Detailed Market View**: Double-click any market for detailed analysis
- **⚙️ Easy Configuration**: Built-in settings panel for API configuration
- **🌐 Live Data Access**: Connects directly to Kalshi API for real-time market data

## 🚀 Quick Start

### Option 1: One-Command Launch (Recommended)

```bash
cd kalshi-analyzer
./run-mac-app.sh
```

This script will automatically:
- Create a Python virtual environment
- Install all dependencies
- Set up your configuration
- Launch the application

### Option 2: Manual Setup

1. **Install Python 3** (if not already installed):
   ```bash
   # Check if Python 3 is installed
   python3 --version

   # If not installed, download from:
   # https://www.python.org/downloads/
   ```

2. **Create a virtual environment**:
   ```bash
   cd kalshi-analyzer
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your Kalshi credentials**:
   ```bash
   cp .env.example .env
   open -t .env
   ```

   Edit the `.env` file and add your Kalshi credentials:
   ```
   KALSHI_EMAIL=your-email@example.com
   KALSHI_PASSWORD=your-password
   KALSHI_DEMO_MODE=true  # Set to 'false' for real trading
   ```

5. **Launch the application**:
   ```bash
   python3 mac_app.py
   ```

## 🎮 How to Use

### Main Interface

1. **Select Number of Markets**: Choose how many markets to analyze (20, 50, 100, or 200)
2. **Click "Analyze Markets"**: Fetches and analyzes live market data
3. **View Results**:
   - **Top Opportunities** tab shows the 10 best betting opportunities
   - **All Markets** tab shows all analyzed markets in a table
   - **Settings** tab for configuration

### Live Auto-Refresh

Enable real-time market monitoring:

1. Check the **"Auto-refresh"** checkbox
2. Select your preferred **refresh interval**:
   - 30 seconds (for active trading)
   - 60 seconds (recommended)
   - 2 minutes (moderate monitoring)
   - 5 minutes (casual monitoring)
3. The app will automatically fetch fresh data at your chosen interval

The status indicator shows:
- **● Ready** (Green) - Ready to analyze
- **● Analyzing...** (Orange) - Fetching live data
- **● Analysis Complete** (Green) - Data is up-to-date
- **● Error** (Red) - Check your configuration

### Market Details

- **Double-click any market** in the All Markets table to see detailed analysis
- View complete pricing data, volume, spreads, and analysis factors

### Understanding the Analysis

The app scores each market from 0-10 based on:
- **Volume & Liquidity**: Higher volume = more reliable prices
- **Spread Analysis**: Tight spreads indicate market efficiency
- **Probability Mispricing**: Identifies potential arbitrage opportunities
- **Time to Close**: Considers when the market resolves
- **Market Characteristics**: Extreme probabilities and other factors

**Score Guide**:
- **7.5-10**: 🔥 STRONG BUY - High-value opportunities
- **6.5-7.4**: 💰 BUY - Good betting opportunities
- **5.5-6.4**: 🤔 CONSIDER - Worth investigating
- **4.0-5.4**: 😐 PASS - Not compelling
- **0-3.9**: ❌ AVOID - Poor opportunity

## 🔒 Demo vs Production Mode

### Demo Mode (Paper Trading) - **Recommended for Testing**
- Set `KALSHI_DEMO_MODE=true` in `.env`
- Uses Kalshi's demo/sandbox environment
- No real money involved
- Perfect for learning and testing strategies

### Production Mode (Real Money) - **Use with Caution**
- Set `KALSHI_DEMO_MODE=false` in `.env`
- Uses real Kalshi markets
- Real money trading
- ⚠️ **Use at your own risk**

## 📦 Creating a Standalone Mac App (Advanced)

Want to create a double-clickable Mac application? Use `py2app`:

```bash
# Install py2app
pip install py2app

# Create setup file
python3 setup.py py2app

# Your app will be in: dist/KalshiBetAnalyzer.app
# Double-click to run!
```

You can then:
- Move the `.app` to your Applications folder
- Pin it to your Dock
- Launch it like any other Mac app

## 🎨 macOS Integration

The app features:
- **Native macOS appearance** with SF Pro fonts
- **Retina-ready** high-resolution interface
- **Dark mode support** (respects system preferences)
- **macOS window controls** and behavior
- **Keyboard shortcuts** (Cmd+Q to quit, etc.)

## 🔧 Troubleshooting

### "Python 3 not found"
Install Python 3 from [python.org](https://www.python.org/downloads/)

### "Configuration Error"
Make sure you've:
1. Created a `.env` file (copy from `.env.example`)
2. Added your Kalshi email and password
3. Saved the file

### "Module not found"
Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### App won't launch
Make sure you're using Python 3.8 or later:
```bash
python3 --version
```

### "Connection Error"
Check that:
- You have internet connectivity
- Your Kalshi credentials are correct
- Kalshi's API is operational

## ⚡ Performance Tips

- **For active trading**: Use 30-60 second auto-refresh
- **For monitoring**: Use 2-5 minute auto-refresh
- **Analyzing 200+ markets**: May take 30-60 seconds to fetch all data
- **Analyzing 20-50 markets**: Very fast, usually under 10 seconds

## 🆘 Support

If you encounter issues:

1. Check the **Settings** tab for configuration status
2. Review the status bar at the bottom for error messages
3. Check the Terminal/Console for detailed error logs
4. Verify your `.env` file is configured correctly

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**.

- Not financial advice
- Past performance doesn't guarantee future results
- Always do your own research (DYOR)
- Only bet what you can afford to lose
- Prediction markets involve risk

## 📱 Want to Use on iPhone?

Check out **[DEPLOY.md](DEPLOY.md)** for cloud deployment options that work on any device!

## 🛠️ Technical Details

- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (native to Python)
- **API Client**: kalshi-python
- **Fonts**: SF Pro (macOS system fonts)
- **Threading**: Multi-threaded for responsive UI during analysis
- **Auto-refresh**: Timer-based background updates

---

**Built with ❤️ for macOS**

Happy betting! 🎰
