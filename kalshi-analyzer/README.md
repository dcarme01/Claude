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
