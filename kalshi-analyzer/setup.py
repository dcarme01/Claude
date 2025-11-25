"""
Setup script for creating macOS application bundle
Usage: python3 setup.py py2app
"""

from setuptools import setup

APP = ['mac_app.py']
DATA_FILES = [
    ('', ['.env.example']),
]

OPTIONS = {
    'argv_emulation': False,
    'iconfile': None,  # Add 'icon.icns' here if you have an icon
    'plist': {
        'CFBundleName': 'Kalshi Bet Analyzer',
        'CFBundleDisplayName': 'Kalshi Bet Analyzer',
        'CFBundleGetInfoString': 'Analyze Kalshi prediction markets',
        'CFBundleIdentifier': 'com.kalshi.analyzer',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': 'Educational purposes only',
        'NSHighResolutionCapable': True,
    },
    'packages': ['tkinter', 'dotenv', 'kalshi_python'],
    'includes': ['analyzer'],
}

setup(
    name='KalshiBetAnalyzer',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'kalshi-python>=2.1.4',
        'python-dotenv>=1.0.0',
    ],
)
