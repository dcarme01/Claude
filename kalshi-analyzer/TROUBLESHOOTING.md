# 🔧 Troubleshooting Guide

If the Kalshi Bet Analyzer isn't working, follow these steps to diagnose and fix the issue.

## 🔍 Step 1: Run the Diagnostic Script

First, let's check if your system is properly set up:

```bash
cd ~/Claude/kalshi-analyzer
python3 test_setup.py
```

This will check:
- Python version
- tkinter (GUI library)
- Required packages
- .env configuration
- Kalshi API connection

Fix any issues it reports before continuing.

## ❌ Common Issues & Solutions

### Issue 1: "No such file or directory: ./run-mac-app.sh"

**Problem**: The code hasn't been downloaded to your Mac yet.

**Solution**:
```bash
# Clone or update the repository
cd ~
git clone https://github.com/dcarme01/Claude.git
cd Claude
git checkout claude/kalshi-bet-analyzer-01Gt2xHUNYmkLS2RzvFEkZo1
cd kalshi-analyzer
./run-mac-app.sh
```

### Issue 2: "ModuleNotFoundError: No module named 'tkinter'"

**Problem**: tkinter isn't installed (GUI library for Python).

**Solution**:

On macOS with Homebrew:
```bash
brew install python-tk
```

Or reinstall Python with tkinter support:
```bash
brew reinstall python@3.11
```

### Issue 3: "Configuration Error" or "Please set KALSHI_EMAIL and KALSHI_PASSWORD"

**Problem**: Your .env file is missing or not configured.

**Solution**:
```bash
cd ~/Claude/kalshi-analyzer

# Create .env from example
cp .env.example .env

# Edit the file
open -e .env
```

In the .env file, replace:
```
KALSHI_EMAIL=your_email@example.com
KALSHI_PASSWORD=your_password
```

With your actual Kalshi credentials:
```
KALSHI_EMAIL=yourreal@email.com
KALSHI_PASSWORD=YourActualPassword123
KALSHI_DEMO_MODE=true
```

Save and try again.

### Issue 4: "kalshi_python module not found"

**Problem**: Dependencies aren't installed.

**Solution**:
```bash
cd ~/Claude/kalshi-analyzer
pip install -r requirements.txt
```

Or let the launcher do it:
```bash
./run-mac-app.sh
```

### Issue 5: App window appears then immediately closes

**Problem**: There's likely an error in initialization.

**Solution**: Run the app directly to see error messages:
```bash
cd ~/Claude/kalshi-analyzer
python3 mac_app.py
```

Read the error message and follow the instructions.

### Issue 6: "Connection Error" or "API Error"

**Problem**: Can't connect to Kalshi API.

**Solutions**:
1. Check your internet connection
2. Verify your Kalshi credentials are correct
3. Make sure you have a Kalshi account at [kalshi.com](https://kalshi.com)
4. Try demo mode: Set `KALSHI_DEMO_MODE=true` in your .env file

### Issue 7: "Font not found" or display looks weird

**Problem**: SF Pro fonts not available on your system.

**Solution**: The app will automatically fall back to Helvetica. This is normal and won't affect functionality.

### Issue 8: Permission denied when running ./run-mac-app.sh

**Problem**: Script isn't executable.

**Solution**:
```bash
chmod +x run-mac-app.sh
./run-mac-app.sh
```

## 🧪 Manual Testing

If the launcher script isn't working, try running manually:

```bash
cd ~/Claude/kalshi-analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configure .env
cp .env.example .env
open -e .env
# (Edit and save with your credentials)

# Run the app
python3 mac_app.py
```

## 🔍 Check Python Version

The app requires Python 3.8 or higher:

```bash
python3 --version
```

If you have an older version:
```bash
brew install python@3.11
```

## 📝 Check File Locations

Make sure you're in the right directory:

```bash
# Should show: /Users/yourusername/Claude/kalshi-analyzer
pwd

# Should show all the app files
ls -la
```

You should see:
- mac_app.py
- analyzer.py
- run-mac-app.sh
- .env.example
- requirements.txt

## 🆘 Still Not Working?

1. **Run the diagnostic**: `python3 test_setup.py`
2. **Check the full error message** - it usually tells you exactly what's wrong
3. **Verify you have a Kalshi account** at [kalshi.com](https://kalshi.com)
4. **Try the web interface instead**: `./start-mobile.sh` (simpler, no tkinter needed)

## 📱 Alternative: Use the Web Interface

If the desktop app won't work, the web interface is simpler:

```bash
cd ~/Claude/kalshi-analyzer
./start-mobile.sh
```

Then open your browser to `http://localhost:5000`

## 💡 Quick Sanity Check

Run these commands and check the output:

```bash
# Should show Python 3.8+
python3 --version

# Should list files including mac_app.py
ls ~/Claude/kalshi-analyzer/

# Should show your configuration
cat ~/Claude/kalshi-analyzer/.env

# Should import successfully
python3 -c "import tkinter; print('tkinter OK')"

# Should import successfully
python3 -c "from kalshi_python import KalshiClient; print('kalshi-python OK')"
```

If any of these fail, that's your issue!

## 📞 Getting More Help

If you're still stuck:
1. Note the exact error message you're seeing
2. Check which step in the diagnostic fails
3. Verify you've followed all setup steps in MAC_SETUP.md
