# 🎰 Complete Setup & Usage Guide

## ✅ Code Verification: Live Data Confirmed

**The website DOES work with live information!** Here's how:

1. **Live Market Data**: Connects directly to Kalshi API to fetch real-time active markets
2. **Real-Time Pricing**: Gets current YES/NO bid/ask prices every time you click "Analyze"
3. **Fresh Analysis**: Analyzes live volume, spreads, and market conditions
4. **No Caching**: Every click fetches brand new data from Kalshi

---

## 🚀 Quick Setup (2 Minutes)

### Step 1: Get the Code

```bash
cd ~/Claude
git pull
cd kalshi-analyzer
```

### Step 2: Run the Setup Script

```bash
./setup.sh
```

This will:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies (including cryptography)
- ✅ Create your .env configuration file
- ✅ Test everything works

**When the .env file opens**, replace with your real Kalshi credentials:

```
KALSHI_EMAIL=your_actual_email@gmail.com
KALSHI_PASSWORD=YourActualPassword123
KALSHI_DEMO_MODE=true
```

Save the file (Cmd+S) and press Enter to continue.

### Step 3: Start the Web App

```bash
./start-web.sh
```

### Step 4: Open Your Browser

Go to: **http://localhost:5000**

**That's it!** 🎉

---

## 📱 How to Use the Website

### Getting Live Analysis

1. **Click "🔍 Analyze Markets"** button
2. **Wait 10-30 seconds** while it fetches live data from Kalshi
3. **View results** - sorted by score (best opportunities first)

### Understanding the Results

Each market card shows:

- **Score (0-10)**: Overall opportunity rating
  - 🔥 **7.5-10**: STRONG BUY - Best opportunities
  - 💰 **6.5-7.4**: BUY - Good opportunities
  - 🤔 **5.5-6.4**: CONSIDER - Worth investigating
  - 😐 **4.0-5.4**: PASS - Not compelling
  - ❌ **0-3.9**: AVOID - Poor opportunity

- **YES/NO Prices**: Current market prices in cents
  - Example: "45¢" means 45% probability / $0.45 per share
  - Bid = Price you'd get selling
  - Ask = Price you'd pay buying

- **Volume**: How many contracts traded (higher = more liquid)
- **Spread**: Difference between bid/ask (lower = better)
- **Analysis Factors**: Why this market got its score

### What Makes a Good Bet?

The analyzer looks for:

✅ **High volume** - More reliable, easier to trade
✅ **Tight spreads** - Lower transaction costs
✅ **Mispricing** - When YES + NO prices don't add up to $1
✅ **Extreme probabilities** - Often mispriced
✅ **Closing soon** - Less time for things to change

---

## 🔴 Live Data Features

### How It Gets Live Information

1. **Click "Analyze Markets"**
2. App connects to Kalshi API (demo.kalshi.com or trade-api.kalshi.com)
3. Fetches current active markets
4. Gets real-time:
   - Current bid/ask prices
   - Trading volume
   - Open interest
   - Time until market closes
5. Analyzes each market
6. Displays results sorted by score

### Refreshing Data

- **Manual Refresh**: Click "Analyze Markets" again anytime
- **Each click fetches new data** - no caching, always fresh
- **Recommended**: Refresh every few minutes during active trading

---

## ⚙️ Configuration Options

### Demo vs Production Mode

Edit your `.env` file:

**Demo Mode** (Recommended):
```
KALSHI_DEMO_MODE=true
```
- Uses Kalshi's sandbox environment
- Paper trading only (no real money)
- Perfect for testing and learning
- Same market structure, may have different data

**Production Mode** (Real Money):
```
KALSHI_DEMO_MODE=false
```
- Uses real Kalshi markets
- Real money trading
- ⚠️ **Only use if you're ready to trade real funds**

### Analyzing More/Fewer Markets

The website analyzes 50 markets by default. To change this, edit `templates/index.html`:

Find line 460:
```javascript
const response = await fetch('/api/analyze?limit=50');
```

Change `50` to:
- `20` - Faster, fewer markets
- `100` - More comprehensive
- `200` - Very thorough (takes longer)

---

## 🔍 Troubleshooting

### "Error: Please set KALSHI_EMAIL and KALSHI_PASSWORD"

Your .env file isn't configured:

```bash
cd ~/Claude/kalshi-analyzer
open -e .env
```

Add your real Kalshi credentials and save.

### "ModuleNotFoundError: No module named 'X'"

Reinstall dependencies:

```bash
cd ~/Claude/kalshi-analyzer
source venv/bin/activate
pip install -r requirements.txt
```

### "HTTP ERROR 403"

The app isn't starting correctly. Check what error you see:

```bash
cd ~/Claude/kalshi-analyzer
source venv/bin/activate
python3 app.py
```

Read the error message - it will tell you what's wrong.

### "Connection Error" or API Errors

1. Check your internet connection
2. Verify your Kalshi credentials are correct
3. Make sure you have a Kalshi account at [kalshi.com](https://kalshi.com)
4. Try demo mode: `KALSHI_DEMO_MODE=true`

### Want More Details?

Run the diagnostic:
```bash
python3 test_setup.py
```

See full troubleshooting guide:
```bash
cat TROUBLESHOOTING.md
```

---

## 📊 What the Code Does

### Key Files

1. **`analyzer.py`** - Core analysis engine
   - Fetches live markets from Kalshi API
   - Analyzes each market based on volume, spread, pricing
   - Scores opportunities 0-10

2. **`app.py`** - Web server
   - Flask web application
   - API endpoint `/api/analyze` returns live analysis
   - Serves the frontend interface

3. **`templates/index.html`** - Frontend website
   - Beautiful, mobile-responsive interface
   - Fetches data from `/api/analyze`
   - Displays results with live pricing

4. **`.env`** - Your credentials (DO NOT share this file!)
   - Kalshi email and password
   - Demo vs production mode setting

### How Live Data Works

```
[You click button]
    ↓
[JavaScript calls /api/analyze]
    ↓
[Flask app calls analyzer.analyze_all_markets()]
    ↓
[Analyzer calls Kalshi API]
    ↓
[Kalshi returns live market data]
    ↓
[Analyzer processes and scores each market]
    ↓
[Flask returns JSON to frontend]
    ↓
[Website displays beautiful results]
```

**Every step happens fresh each time you click!**

---

## 🎯 Pro Tips

1. **Start with demo mode** until you understand how it works
2. **Refresh every 2-5 minutes** during active trading
3. **Focus on scores 7+** for best opportunities
4. **Read the analysis factors** - they explain the "why"
5. **Check volume** - higher is better for actually trading
6. **Watch the spread** - lower means less cost to trade
7. **Do your own research** - this is a tool, not financial advice!

---

## 🆘 Need Help?

### Quick Checks

```bash
# Make sure you're in the right place
cd ~/Claude/kalshi-analyzer
pwd

# Check Python version (need 3.8+)
python3 --version

# Test configuration
python3 test_setup.py

# View your .env settings
cat .env

# Reinstall everything
./setup.sh
```

### Common Commands

```bash
# Complete fresh setup
./setup.sh

# Start the web app
./start-web.sh

# Run with debug output
python3 app.py
```

---

## ⚠️ Important Notes

### This Tool Is For:
- ✅ Educational purposes
- ✅ Learning about prediction markets
- ✅ Identifying potential opportunities
- ✅ Understanding market dynamics

### This Tool Is NOT:
- ❌ Financial advice
- ❌ A guaranteed profit system
- ❌ A replacement for your own research
- ❌ Responsible for your trading decisions

### Always Remember:
- Past performance ≠ future results
- Markets can change quickly
- Only bet what you can afford to lose
- Do your own research (DYOR)
- Understand the risks involved

---

## 🎓 Don't Have a Kalshi Account?

1. Go to [kalshi.com](https://kalshi.com)
2. Sign up for a free account
3. Verify your email
4. (Optional) Add funds if you want to trade with real money
5. Use those credentials in your `.env` file

**Start with demo mode** to practice first!

---

## ✅ Verification Checklist

Before using, make sure:

- [ ] Python 3.8+ installed
- [ ] Ran `./setup.sh` successfully
- [ ] Created `.env` file with real Kalshi credentials
- [ ] `python3 test_setup.py` shows all green checkmarks
- [ ] Can start app with `./start-web.sh`
- [ ] Browser opens to http://localhost:5000
- [ ] Clicking "Analyze Markets" returns results
- [ ] Results show live market data with prices

---

**Ready to analyze some markets?** 🎰

```bash
./start-web.sh
```

Then open: **http://localhost:5000**

Happy trading! 📈
