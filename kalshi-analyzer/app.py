#!/usr/bin/env python3
"""
Kalshi Bet Analyzer - Web Interface
Flask app for viewing Kalshi market analysis
"""

import os
from flask import Flask, render_template, jsonify, request
from analyzer import KalshiAnalyzer
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Global analyzer instance
analyzer = None


def get_analyzer():
    """Get or create analyzer instance"""
    global analyzer
    if analyzer is None:
        demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
        analyzer = KalshiAnalyzer(demo_mode=demo_mode)
    return analyzer


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/analyze')
def analyze():
    """API endpoint to get market analysis"""
    try:
        limit = int(request.args.get('limit', 50))
        analyzer = get_analyzer()
        analyses = analyzer.analyze_all_markets(limit=limit)

        # Convert to JSON-friendly format
        results = []
        for analysis in analyses:
            results.append({
                'ticker': analysis['ticker'],
                'title': analysis['title'],
                'score': analysis['score'],
                'recommendation': analysis['recommendation'],
                'emoji': analysis['emoji'],
                'yes_price': analysis['yes_price'],
                'no_price': analysis['no_price'],
                'yes_bid': analysis['yes_bid'],
                'yes_ask': analysis['yes_ask'],
                'no_bid': analysis['no_bid'],
                'no_ask': analysis['no_ask'],
                'spread': analysis['spread'],
                'volume': analysis['volume'],
                'open_interest': analysis['open_interest'],
                'factors': analysis['factors'],
                'close_time': analysis['close_time']
            })

        return jsonify({
            'success': True,
            'count': len(results),
            'analyses': results
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/status')
def status():
    """API endpoint to check status"""
    try:
        demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
        return jsonify({
            'success': True,
            'demo_mode': demo_mode,
            'configured': bool(os.getenv('KALSHI_EMAIL') and os.getenv('KALSHI_PASSWORD'))
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("🎰 Starting Kalshi Bet Analyzer Web Interface")
    print("=" * 60)
    print()
    print("📱 Open your browser to: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop")
    print()

    app.run(debug=True, host='0.0.0.0', port=5000)
