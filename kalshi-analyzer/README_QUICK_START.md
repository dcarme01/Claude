# ⚡ Quick Start Guide - macOS

Get the Kalshi Bet Analyzer running in under 5 minutes!

## 🚀 Super Quick Start

```bash
cd ~/Claude/kalshi-analyzer
./run-mac-app.sh
```

**That's it!** The script handles everything automatically.

---

## 📋 What You Need

1. **A Mac** running macOS
2. **Python 3.8+** (usually pre-installed on modern Macs)
3. **A Kalshi account** from [kalshi.com](https://kalshi.com) (free to sign up)
4. **5 minutes** of your time

---

## 🎯 Step-by-Step First Time Setup

### 1. Get the Code

If you haven't cloned the repository yet:

```bash
cd ~
git clone https://github.com/dcarme01/Claude.git
cd Claude/kalshi-analyzer
```

If you already have it, just update:

```bash
cd ~/Claude
git pull
cd kalshi-analyzer
```

### 2. Configure Your Credentials

```bash
# Copy the example file
cp .env.example .env

# Edit it
open -e .env
```

Change these lines:
```
KALSHI_EMAIL=your_email@example.com    # Change this!
KALSHI_PASSWORD=your_password          # Change this!
KALSHI_DEMO_MODE=true                  # Keep this for testing
```

**Save the file** (Cmd+S) and close TextEdit.

### 3. Run the App

```bash
./run-mac-app.sh
```

**Done!** The app will:
- Install Python dependencies automatically
- Connect to Kalshi
- Open the desktop application

---

## 🐛 Something Not Working?

### Try the diagnostic tool:

```bash
python3 test_setup.py
```

This will tell you exactly what's wrong.

### Or run in debug mode:

```bash
./run-mac-app-debug.sh
```

This shows full error messages.

### Still stuck?

See **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** for detailed solutions to common issues.

---

## 🎮 Using the App

Once the app opens:

1. **Select number of markets** (20, 50, 100, or 200)
2. **Click "Analyze Markets"** to fetch live data
3. **Enable "Auto-refresh"** for continuous updates
4. **View results** in two tabs:
   - **Top Opportunities**: Best 10 bets
   - **All Markets**: Complete sortable table

### Auto-Refresh Feature

- Check "Auto-refresh" in the top toolbar
- Select interval: 30s, 60s, 2min, or 5min
- App automatically fetches new data!

---

## 📱 Other Options

### Menu Bar App (Lightweight)
```bash
./run-menubar.sh
```

Quick access from your Mac menu bar!

### Web Interface (Browser-based)
```bash
./start-mobile.sh
```

Then open: `http://localhost:5000`

### Command Line (One-time Analysis)
```bash
python3 analyzer.py
```

---

## ⚙️ Demo vs Production Mode

**Demo Mode** (Recommended):
- Set `KALSHI_DEMO_MODE=true`
- Paper trading only
- No real money
- Perfect for learning

**Production Mode** (Real Money):
- Set `KALSHI_DEMO_MODE=false`
- Real Kalshi markets
- ⚠️ Use at your own risk

---

## 🔑 Don't Have a Kalshi Account Yet?

1. Go to [kalshi.com](https://kalshi.com)
2. Sign up (it's free!)
3. Use those credentials in your `.env` file
4. Start with `KALSHI_DEMO_MODE=true` to practice

---

## 💡 Pro Tips

1. **Start with 20-50 markets** - it's faster
2. **Use demo mode** until you're comfortable
3. **Enable auto-refresh at 60s** for active monitoring
4. **Double-click any market** in the table for detailed analysis
5. **Read the "Factors"** - they explain why each bet is scored

---

## 🆘 Quick Help Commands

```bash
# Check if everything is installed correctly
python3 test_setup.py

# Run with debug output
./run-mac-app-debug.sh

# Check Python version (need 3.8+)
python3 --version

# View your .env configuration
cat .env

# Reinstall dependencies
pip install -r requirements.txt
```

---

## ✅ Checklist

Before asking for help, make sure you've:

- [ ] Cloned/updated the repository
- [ ] Created a `.env` file from `.env.example`
- [ ] Added your real Kalshi email and password to `.env`
- [ ] Have Python 3.8 or higher installed
- [ ] Ran `python3 test_setup.py` successfully
- [ ] Are in the `kalshi-analyzer` directory

---

**Ready? Let's go!**

```bash
./run-mac-app.sh
```

🎰 Happy analyzing!
