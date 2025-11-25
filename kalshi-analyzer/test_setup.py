#!/usr/bin/env python3
"""
Diagnostic script to test if your system is ready to run the Kalshi Analyzer
"""

import sys

print("🔍 Kalshi Bet Analyzer - System Check")
print("=" * 60)
print()

# Check Python version
print("1. Checking Python version...")
print(f"   Python {sys.version}")
if sys.version_info < (3, 8):
    print("   ❌ ERROR: Python 3.8 or higher is required")
    sys.exit(1)
else:
    print("   ✅ Python version OK")
print()

# Check tkinter
print("2. Checking tkinter (GUI library)...")
try:
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    root.destroy()
    print("   ✅ tkinter is working")
except ImportError:
    print("   ❌ ERROR: tkinter is not installed")
    print("   Install it with:")
    print("   brew install python-tk@3.11  (adjust version as needed)")
    sys.exit(1)
except Exception as e:
    print(f"   ❌ ERROR: tkinter test failed: {e}")
    sys.exit(1)
print()

# Check required packages
print("3. Checking required packages...")
required_packages = {
    'kalshi_python': 'kalshi-python',
    'dotenv': 'python-dotenv',
    'flask': 'flask'
}

missing = []
for module, package in required_packages.items():
    try:
        __import__(module)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} not installed")
        missing.append(package)

if missing:
    print()
    print("   Install missing packages with:")
    print(f"   pip install {' '.join(missing)}")
    sys.exit(1)
print()

# Check .env file
print("4. Checking .env configuration...")
import os
from dotenv import load_dotenv

load_dotenv()

if not os.path.exists('.env'):
    print("   ⚠️  WARNING: .env file not found")
    print("   Create one with: cp .env.example .env")
else:
    print("   ✅ .env file exists")

    email = os.getenv('KALSHI_EMAIL')
    password = os.getenv('KALSHI_PASSWORD')

    if not email or 'your_email' in email:
        print("   ⚠️  WARNING: KALSHI_EMAIL not configured")
    else:
        print(f"   ✅ KALSHI_EMAIL: {email}")

    if not password or 'your_password' in password:
        print("   ⚠️  WARNING: KALSHI_PASSWORD not configured")
    else:
        print(f"   ✅ KALSHI_PASSWORD: {'*' * len(password)}")

    demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true')
    print(f"   ℹ️  KALSHI_DEMO_MODE: {demo_mode}")
print()

# Check Kalshi connection
print("5. Testing Kalshi API connection...")
try:
    from analyzer import KalshiAnalyzer

    if not os.getenv('KALSHI_EMAIL') or 'your_email' in os.getenv('KALSHI_EMAIL', ''):
        print("   ⚠️  SKIPPED: Credentials not configured yet")
    else:
        demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
        analyzer = KalshiAnalyzer(demo_mode=demo_mode)
        print("   ✅ Kalshi API connection successful")
except ValueError as e:
    print(f"   ⚠️  SKIPPED: {e}")
except Exception as e:
    print(f"   ❌ ERROR: {e}")
print()

print("=" * 60)
print("✅ System check complete!")
print()
print("Next steps:")
if not os.path.exists('.env'):
    print("  1. Create .env file: cp .env.example .env")
    print("  2. Edit .env and add your Kalshi credentials")
    print("  3. Run: ./run-mac-app.sh")
elif not os.getenv('KALSHI_EMAIL') or 'your_email' in os.getenv('KALSHI_EMAIL', ''):
    print("  1. Edit .env and add your real Kalshi credentials")
    print("  2. Run: ./run-mac-app.sh")
else:
    print("  Your system is ready! Run: ./run-mac-app.sh")
print()
