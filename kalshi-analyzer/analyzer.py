#!/usr/bin/env python3
"""
Kalshi Bet Analyzer
Analyzes prediction markets to identify profitable opportunities
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv
from kalshi_python import KalshiClient

# Load environment variables
load_dotenv()


class KalshiAnalyzer:
    """Analyzes Kalshi markets for profitable betting opportunities"""

    def __init__(self, demo_mode=True):
        """Initialize the Kalshi analyzer

        Args:
            demo_mode: If True, use demo environment. False for production.
        """
        email = os.getenv('KALSHI_EMAIL')
        password = os.getenv('KALSHI_PASSWORD')

        if not email or not password:
            raise ValueError(
                "Please set KALSHI_EMAIL and KALSHI_PASSWORD in .env file"
            )

        # Initialize Kalshi client
        if demo_mode:
            print("🔧 Using DEMO mode (paper trading)")
            self.client = KalshiClient(email, password, demo=True)
        else:
            print("⚠️  Using PRODUCTION mode (real money)")
            self.client = KalshiClient(email, password, demo=False)

        self.demo_mode = demo_mode

    def fetch_active_markets(self, limit=100) -> List[Dict[str, Any]]:
        """Fetch active markets from Kalshi

        Args:
            limit: Maximum number of markets to fetch

        Returns:
            List of market dictionaries
        """
        try:
            print(f"📊 Fetching active markets (limit: {limit})...")

            # Get active markets
            response = self.client.get_markets(
                limit=limit,
                status='active'
            )

            markets = response.get('markets', [])
            print(f"✅ Found {len(markets)} active markets")

            return markets
        except Exception as e:
            print(f"❌ Error fetching markets: {e}")
            return []

    def analyze_market(self, market: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a single market for profitability

        Args:
            market: Market data dictionary

        Returns:
            Analysis results with score and reasoning
        """
        ticker = market.get('ticker', 'UNKNOWN')
        title = market.get('title', 'Unknown Market')

        # Extract key metrics
        yes_bid = market.get('yes_bid', 0) / 100 if market.get('yes_bid') else 0
        yes_ask = market.get('yes_ask', 0) / 100 if market.get('yes_ask') else 0
        no_bid = market.get('no_bid', 0) / 100 if market.get('no_bid') else 0
        no_ask = market.get('no_ask', 0) / 100 if market.get('no_ask') else 0

        volume = market.get('volume', 0)
        open_interest = market.get('open_interest', 0)
        close_time = market.get('close_time', '')

        # Calculate metrics
        yes_mid = (yes_bid + yes_ask) / 2 if yes_ask > 0 else 0
        no_mid = (no_bid + no_ask) / 2 if no_ask > 0 else 0

        yes_spread = yes_ask - yes_bid if yes_ask and yes_bid else 0
        no_spread = no_ask - no_bid if no_ask and no_bid else 0

        # Analysis factors
        factors = []
        score = 5.0  # Start with neutral score

        # Factor 1: Liquidity (volume and open interest)
        if volume > 10000:
            score += 1.5
            factors.append("✅ High volume (good liquidity)")
        elif volume > 1000:
            score += 0.5
            factors.append("📊 Moderate volume")
        else:
            score -= 1.0
            factors.append("⚠️ Low volume (poor liquidity)")

        # Factor 2: Spread analysis
        avg_spread = (yes_spread + no_spread) / 2
        if avg_spread < 0.05:
            score += 1.0
            factors.append("✅ Tight spread (efficient market)")
        elif avg_spread < 0.10:
            score += 0.5
            factors.append("📊 Moderate spread")
        else:
            score -= 0.5
            factors.append("⚠️ Wide spread (inefficient)")

        # Factor 3: Probability check (should sum close to 1.0)
        prob_sum = yes_mid + no_mid
        if abs(prob_sum - 1.0) > 0.15:
            score += 2.0
            factors.append(f"🎯 ARBITRAGE OPPORTUNITY! Probabilities sum to {prob_sum:.2f}")
        elif abs(prob_sum - 1.0) > 0.05:
            score += 1.0
            factors.append(f"💡 Potential mispricing (sum={prob_sum:.2f})")
        else:
            factors.append(f"Fair pricing (sum={prob_sum:.2f})")

        # Factor 4: Extreme probabilities (often mispriced)
        if 0.05 < yes_mid < 0.15 or 0.85 < yes_mid < 0.95:
            score += 0.5
            factors.append("💡 Extreme probability (potential value)")

        # Factor 5: Time to close
        if close_time:
            try:
                close_dt = datetime.fromisoformat(close_time.replace('Z', '+00:00'))
                now = datetime.now(close_dt.tzinfo)
                hours_to_close = (close_dt - now).total_seconds() / 3600

                if hours_to_close < 24:
                    score += 0.5
                    factors.append(f"⏰ Closes soon ({hours_to_close:.1f}h)")
                elif hours_to_close < 72:
                    factors.append(f"📅 Closes in {hours_to_close/24:.1f} days")
                else:
                    score -= 0.5
                    factors.append(f"📅 Long duration ({hours_to_close/24:.0f} days)")
            except:
                factors.append("📅 Unknown close time")

        # Cap score between 0-10
        score = max(0, min(10, score))

        # Determine recommendation
        if score >= 7.5:
            recommendation = "STRONG BUY"
            emoji = "🔥"
        elif score >= 6.5:
            recommendation = "BUY"
            emoji = "💰"
        elif score >= 5.5:
            recommendation = "CONSIDER"
            emoji = "🤔"
        elif score >= 4.0:
            recommendation = "PASS"
            emoji = "😐"
        else:
            recommendation = "AVOID"
            emoji = "❌"

        return {
            'ticker': ticker,
            'title': title,
            'score': round(score, 1),
            'recommendation': recommendation,
            'emoji': emoji,
            'yes_price': yes_mid,
            'no_price': no_mid,
            'yes_bid': yes_bid,
            'yes_ask': yes_ask,
            'no_bid': no_bid,
            'no_ask': no_ask,
            'spread': avg_spread,
            'volume': volume,
            'open_interest': open_interest,
            'factors': factors,
            'close_time': close_time,
            'raw_market': market
        }

    def analyze_all_markets(self, limit=100) -> List[Dict[str, Any]]:
        """Fetch and analyze all active markets

        Args:
            limit: Maximum number of markets to fetch

        Returns:
            List of analyzed markets, sorted by score
        """
        markets = self.fetch_active_markets(limit)

        if not markets:
            print("⚠️ No markets found to analyze")
            return []

        print(f"\n🔍 Analyzing {len(markets)} markets...\n")

        analyses = []
        for market in markets:
            analysis = self.analyze_market(market)
            analyses.append(analysis)

        # Sort by score (highest first)
        analyses.sort(key=lambda x: x['score'], reverse=True)

        return analyses

    def print_analysis(self, analyses: List[Dict[str, Any]], top_n=10):
        """Print analysis results in a readable format

        Args:
            analyses: List of analysis results
            top_n: Number of top opportunities to display
        """
        if not analyses:
            print("No analyses to display")
            return

        print("=" * 80)
        print(f"{'🎯 TOP KALSHI BETTING OPPORTUNITIES':^80}")
        print("=" * 80)
        print()

        for i, analysis in enumerate(analyses[:top_n], 1):
            print(f"{i}. {analysis['emoji']} {analysis['ticker']}")
            print(f"   {analysis['title'][:70]}")
            print(f"   Score: {analysis['score']}/10 | {analysis['recommendation']}")
            print(f"   YES: {analysis['yes_price']:.2%} (bid: {analysis['yes_bid']:.2%}, ask: {analysis['yes_ask']:.2%})")
            print(f"   NO:  {analysis['no_price']:.2%} (bid: {analysis['no_bid']:.2%}, ask: {analysis['no_ask']:.2%})")
            print(f"   Volume: {analysis['volume']:,} | Spread: {analysis['spread']:.2%}")
            print()
            print("   Factors:")
            for factor in analysis['factors']:
                print(f"     • {factor}")
            print()
            print("-" * 80)
            print()


def main():
    """Main entry point"""
    print("🎰 Kalshi Bet Analyzer")
    print("=" * 80)
    print()

    # Check for demo mode setting
    demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'

    try:
        # Initialize analyzer
        analyzer = KalshiAnalyzer(demo_mode=demo_mode)

        # Analyze markets
        analyses = analyzer.analyze_all_markets(limit=100)

        # Print results
        analyzer.print_analysis(analyses, top_n=10)

        print("✅ Analysis complete!")
        print()
        print("💡 Tip: Markets with scores 7+ are worth investigating further")
        print("⚠️  Always do your own research before placing bets!")

    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print()
        print("Please create a .env file with your Kalshi credentials:")
        print("  cp .env.example .env")
        print("  # Then edit .env with your details")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
