#!/usr/bin/env python3
"""
Kalshi Bet Analyzer - macOS Desktop Application
Native Mac app with live bet analysis and auto-refresh
"""

import os
import sys
import json
import threading
import webbrowser
from datetime import datetime
from typing import Optional
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from dotenv import load_dotenv

# Import the analyzer
from analyzer import KalshiAnalyzer

load_dotenv()


class KalshiMacApp:
    """macOS desktop application for Kalshi bet analysis"""

    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Kalshi Bet Analyzer")
        self.root.geometry("1200x800")

        # Configure for macOS appearance
        self.configure_mac_style()

        # Application state
        self.analyzer: Optional[KalshiAnalyzer] = None
        self.analyses = []
        self.is_analyzing = False
        self.auto_refresh = False
        self.refresh_interval = 60  # seconds
        self.refresh_timer = None

        # Create UI
        self.create_ui()

        # Initialize analyzer
        self.initialize_analyzer()

    def configure_mac_style(self):
        """Configure macOS-specific styling"""
        # Set macOS-friendly colors
        self.bg_color = "#f5f5f5"
        self.accent_color = "#007AFF"
        self.text_color = "#000000"

        # Configure root window
        self.root.configure(bg=self.bg_color)

        # macOS-specific settings
        if sys.platform == 'darwin':
            # Use native macOS appearance
            try:
                self.root.tk.call('tk::unsupported::MacWindowStyle', 'style',
                                self.root._w, 'documentProc')
            except:
                pass

    def create_ui(self):
        """Create the user interface"""
        # Top toolbar
        toolbar = tk.Frame(self.root, bg=self.bg_color, pady=10)
        toolbar.pack(fill=tk.X, padx=10)

        # Title
        try:
            title_font = ("SF Pro Display", 20, "bold")
        except:
            title_font = ("Helvetica", 20, "bold")

        title = tk.Label(toolbar, text="🎰 Kalshi Bet Analyzer",
                        font=title_font,
                        bg=self.bg_color, fg=self.text_color)
        title.pack(side=tk.LEFT, padx=10)

        # Status indicator
        try:
            status_font = ("SF Pro Text", 12)
        except:
            status_font = ("Helvetica", 12)

        self.status_label = tk.Label(toolbar, text="● Ready",
                                     font=status_font,
                                     bg=self.bg_color, fg="#34C759")
        self.status_label.pack(side=tk.LEFT, padx=20)

        # Spacer
        tk.Frame(toolbar, bg=self.bg_color).pack(side=tk.LEFT, expand=True)

        # Auto-refresh toggle
        self.auto_refresh_var = tk.BooleanVar()
        try:
            check_font = ("SF Pro Text", 11)
        except:
            check_font = ("Helvetica", 11)

        auto_refresh_check = tk.Checkbutton(
            toolbar, text="Auto-refresh", variable=self.auto_refresh_var,
            command=self.toggle_auto_refresh,
            bg=self.bg_color, font=check_font,
            activebackground=self.bg_color
        )
        auto_refresh_check.pack(side=tk.RIGHT, padx=5)

        # Refresh interval
        try:
            label_font = ("SF Pro Text", 11)
        except:
            label_font = ("Helvetica", 11)

        tk.Label(toolbar, text="Interval:", bg=self.bg_color,
                font=label_font).pack(side=tk.RIGHT, padx=5)

        self.interval_var = tk.StringVar(value="60")
        interval_options = ["30", "60", "120", "300"]
        interval_menu = ttk.Combobox(toolbar, textvariable=self.interval_var,
                                    values=interval_options, width=6, state="readonly")
        interval_menu.pack(side=tk.RIGHT, padx=5)
        interval_menu.bind('<<ComboboxSelected>>', self.update_interval)

        # Analyze button
        self.analyze_btn = tk.Button(
            toolbar, text="🔍 Analyze Markets",
            command=self.start_analysis,
            bg=self.accent_color, fg="white",
            font=("SF Pro Text", 12, "bold"),
            relief=tk.FLAT, padx=20, pady=8,
            cursor="hand2"
        )
        self.analyze_btn.pack(side=tk.RIGHT, padx=5)

        # Market count selector
        tk.Label(toolbar, text="Markets:", bg=self.bg_color,
                font=("SF Pro Text", 11)).pack(side=tk.RIGHT, padx=5)

        self.market_count_var = tk.StringVar(value="50")
        market_options = ["20", "50", "100", "200"]
        market_menu = ttk.Combobox(toolbar, textvariable=self.market_count_var,
                                   values=market_options, width=6, state="readonly")
        market_menu.pack(side=tk.RIGHT, padx=5)

        # Main content area with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 1: Top Opportunities
        self.opportunities_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.opportunities_frame, text="🔥 Top Opportunities")
        self.create_opportunities_view()

        # Tab 2: All Markets
        self.all_markets_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.all_markets_frame, text="📊 All Markets")
        self.create_all_markets_view()

        # Tab 3: Settings
        self.settings_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.settings_frame, text="⚙️ Settings")
        self.create_settings_view()

        # Bottom status bar
        self.create_status_bar()

    def create_opportunities_view(self):
        """Create the top opportunities view"""
        # Scrollable text area
        self.opportunities_text = scrolledtext.ScrolledText(
            self.opportunities_frame,
            font=("SF Mono", 11),
            bg="white",
            fg=self.text_color,
            wrap=tk.WORD,
            padx=20,
            pady=20
        )
        self.opportunities_text.pack(fill=tk.BOTH, expand=True)

        # Configure tags for formatting
        self.opportunities_text.tag_config("title", font=("SF Pro Display", 16, "bold"))
        self.opportunities_text.tag_config("score", font=("SF Pro Text", 12, "bold"),
                                          foreground="#34C759")
        self.opportunities_text.tag_config("ticker", font=("SF Mono", 11),
                                          foreground="#007AFF")

    def create_all_markets_view(self):
        """Create the all markets table view"""
        # Create treeview for table display
        columns = ("Rank", "Ticker", "Score", "Recommendation", "YES", "NO", "Volume")

        self.markets_tree = ttk.Treeview(self.all_markets_frame, columns=columns,
                                        show='headings', height=20)

        # Configure columns
        self.markets_tree.heading("Rank", text="#")
        self.markets_tree.heading("Ticker", text="Ticker")
        self.markets_tree.heading("Score", text="Score")
        self.markets_tree.heading("Recommendation", text="Recommendation")
        self.markets_tree.heading("YES", text="YES Price")
        self.markets_tree.heading("NO", text="NO Price")
        self.markets_tree.heading("Volume", text="Volume")

        self.markets_tree.column("Rank", width=50)
        self.markets_tree.column("Ticker", width=150)
        self.markets_tree.column("Score", width=70)
        self.markets_tree.column("Recommendation", width=130)
        self.markets_tree.column("YES", width=100)
        self.markets_tree.column("NO", width=100)
        self.markets_tree.column("Volume", width=100)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.all_markets_frame, orient=tk.VERTICAL,
                                 command=self.markets_tree.yview)
        self.markets_tree.configure(yscrollcommand=scrollbar.set)

        # Pack
        self.markets_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind double-click to show details
        self.markets_tree.bind('<Double-1>', self.show_market_details)

    def create_settings_view(self):
        """Create the settings view"""
        settings_container = tk.Frame(self.settings_frame, bg="white")
        settings_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

        # Title
        tk.Label(settings_container, text="⚙️ Application Settings",
                font=("SF Pro Display", 18, "bold"),
                bg="white").pack(anchor=tk.W, pady=(0, 20))

        # API Settings
        api_frame = tk.LabelFrame(settings_container, text="Kalshi API Configuration",
                                 font=("SF Pro Text", 12, "bold"),
                                 bg="white", padx=20, pady=20)
        api_frame.pack(fill=tk.X, pady=10)

        demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
        has_credentials = bool(os.getenv('KALSHI_EMAIL') and os.getenv('KALSHI_PASSWORD'))

        status_text = "✅ Demo Mode (Paper Trading)" if demo_mode else "⚠️ Production Mode (Real Money)"
        tk.Label(api_frame, text=f"Mode: {status_text}",
                font=("SF Pro Text", 11),
                bg="white").pack(anchor=tk.W, pady=5)

        cred_status = "✅ Configured" if has_credentials else "❌ Not Configured"
        tk.Label(api_frame, text=f"Credentials: {cred_status}",
                font=("SF Pro Text", 11),
                bg="white").pack(anchor=tk.W, pady=5)

        tk.Button(api_frame, text="📝 Edit .env File",
                 command=self.open_env_file,
                 bg=self.accent_color, fg="white",
                 font=("SF Pro Text", 11),
                 relief=tk.FLAT, padx=15, pady=5).pack(anchor=tk.W, pady=10)

        # Display Settings
        display_frame = tk.LabelFrame(settings_container, text="Display Settings",
                                     font=("SF Pro Text", 12, "bold"),
                                     bg="white", padx=20, pady=20)
        display_frame.pack(fill=tk.X, pady=10)

        tk.Label(display_frame, text="Default markets to fetch:",
                font=("SF Pro Text", 11),
                bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)

        # About
        about_frame = tk.LabelFrame(settings_container, text="About",
                                   font=("SF Pro Text", 12, "bold"),
                                   bg="white", padx=20, pady=20)
        about_frame.pack(fill=tk.X, pady=10)

        tk.Label(about_frame, text="Kalshi Bet Analyzer for macOS",
                font=("SF Pro Text", 11, "bold"),
                bg="white").pack(anchor=tk.W, pady=2)

        tk.Label(about_frame, text="Analyzes prediction markets in real-time",
                font=("SF Pro Text", 10),
                bg="white", fg="#666").pack(anchor=tk.W, pady=2)

        tk.Label(about_frame, text="⚠️ For educational purposes only. Always DYOR!",
                font=("SF Pro Text", 10),
                bg="white", fg="#FF3B30").pack(anchor=tk.W, pady=10)

    def create_status_bar(self):
        """Create bottom status bar"""
        status_bar = tk.Frame(self.root, bg="#e5e5e5", height=30)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        self.last_update_label = tk.Label(status_bar, text="Last update: Never",
                                         font=("SF Pro Text", 10),
                                         bg="#e5e5e5", fg="#666")
        self.last_update_label.pack(side=tk.LEFT, padx=10)

        self.market_count_label = tk.Label(status_bar, text="Markets: 0",
                                          font=("SF Pro Text", 10),
                                          bg="#e5e5e5", fg="#666")
        self.market_count_label.pack(side=tk.RIGHT, padx=10)

    def initialize_analyzer(self):
        """Initialize the Kalshi analyzer"""
        try:
            demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
            self.analyzer = KalshiAnalyzer(demo_mode=demo_mode)
            self.update_status("✅ Connected to Kalshi", "#34C759")
        except ValueError as e:
            self.update_status("❌ Configuration Error", "#FF3B30")
            messagebox.showerror("Configuration Error",
                               f"Please configure your Kalshi credentials in the .env file.\n\n{str(e)}")
        except Exception as e:
            self.update_status("❌ Error", "#FF3B30")
            messagebox.showerror("Error", f"Failed to initialize analyzer: {str(e)}")

    def start_analysis(self):
        """Start market analysis in background thread"""
        if self.is_analyzing:
            return

        # Run analysis in background thread
        thread = threading.Thread(target=self.analyze_markets, daemon=True)
        thread.start()

    def analyze_markets(self):
        """Analyze markets (runs in background thread)"""
        if not self.analyzer:
            self.root.after(0, lambda: messagebox.showerror("Error",
                                                            "Analyzer not initialized"))
            return

        self.is_analyzing = True
        self.root.after(0, lambda: self.update_status("🔄 Analyzing...", "#FF9500"))
        self.root.after(0, lambda: self.analyze_btn.config(state=tk.DISABLED))

        try:
            # Get market count
            limit = int(self.market_count_var.get())

            # Fetch and analyze
            analyses = self.analyzer.analyze_all_markets(limit=limit)

            # Update UI with results
            self.root.after(0, lambda: self.display_analyses(analyses))
            self.root.after(0, lambda: self.update_status("✅ Analysis Complete", "#34C759"))

            # Update last update time
            now = datetime.now().strftime("%I:%M:%S %p")
            self.root.after(0, lambda: self.last_update_label.config(
                text=f"Last update: {now}"))
            self.root.after(0, lambda: self.market_count_label.config(
                text=f"Markets: {len(analyses)}"))

        except Exception as e:
            self.root.after(0, lambda: self.update_status("❌ Error", "#FF3B30"))
            self.root.after(0, lambda: messagebox.showerror("Analysis Error", str(e)))

        finally:
            self.is_analyzing = False
            self.root.after(0, lambda: self.analyze_btn.config(state=tk.NORMAL))

    def display_analyses(self, analyses):
        """Display analysis results"""
        self.analyses = analyses

        # Update top opportunities view
        self.opportunities_text.delete(1.0, tk.END)

        if not analyses:
            self.opportunities_text.insert(tk.END, "No markets found.\n\n")
            return

        # Show top 10
        self.opportunities_text.insert(tk.END, "🔥 TOP BETTING OPPORTUNITIES\n\n", "title")

        for i, analysis in enumerate(analyses[:10], 1):
            # Market header
            header = f"{i}. {analysis['emoji']} {analysis['ticker']}\n"
            self.opportunities_text.insert(tk.END, header, "ticker")

            # Title
            self.opportunities_text.insert(tk.END, f"{analysis['title']}\n\n")

            # Score and recommendation
            score_text = f"Score: {analysis['score']}/10 | {analysis['recommendation']}\n"
            self.opportunities_text.insert(tk.END, score_text, "score")

            # Prices
            self.opportunities_text.insert(tk.END,
                f"YES: {analysis['yes_price']:.1%} (bid: {analysis['yes_bid']:.1%}, "
                f"ask: {analysis['yes_ask']:.1%})\n")
            self.opportunities_text.insert(tk.END,
                f"NO:  {analysis['no_price']:.1%} (bid: {analysis['no_bid']:.1%}, "
                f"ask: {analysis['no_ask']:.1%})\n")

            # Metrics
            self.opportunities_text.insert(tk.END,
                f"Volume: {analysis['volume']:,} | Spread: {analysis['spread']:.1%}\n\n")

            # Factors
            self.opportunities_text.insert(tk.END, "Factors:\n")
            for factor in analysis['factors']:
                self.opportunities_text.insert(tk.END, f"  • {factor}\n")

            self.opportunities_text.insert(tk.END, "\n" + "─" * 80 + "\n\n")

        # Update table view
        self.update_markets_table(analyses)

    def update_markets_table(self, analyses):
        """Update the markets table"""
        # Clear existing
        for item in self.markets_tree.get_children():
            self.markets_tree.delete(item)

        # Add rows
        for i, analysis in enumerate(analyses, 1):
            emoji = analysis['emoji']
            values = (
                i,
                f"{emoji} {analysis['ticker']}",
                f"{analysis['score']:.1f}",
                analysis['recommendation'],
                f"{analysis['yes_price']:.1%}",
                f"{analysis['no_price']:.1%}",
                f"{analysis['volume']:,}"
            )
            self.markets_tree.insert('', tk.END, values=values, tags=(analysis['ticker'],))

    def show_market_details(self, event):
        """Show detailed market information"""
        selection = self.markets_tree.selection()
        if not selection:
            return

        # Get the ticker from tags
        item = selection[0]
        tags = self.markets_tree.item(item, 'tags')
        if not tags:
            return

        ticker = tags[0]

        # Find the analysis
        analysis = next((a for a in self.analyses if a['ticker'] == ticker), None)
        if not analysis:
            return

        # Show details dialog
        self.show_details_dialog(analysis)

    def show_details_dialog(self, analysis):
        """Show market details in a dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Market Details - {analysis['ticker']}")
        dialog.geometry("600x500")
        dialog.configure(bg="white")

        # Content
        text = scrolledtext.ScrolledText(dialog, font=("SF Mono", 11),
                                        bg="white", wrap=tk.WORD,
                                        padx=20, pady=20)
        text.pack(fill=tk.BOTH, expand=True)

        # Format details
        text.insert(tk.END, f"{analysis['emoji']} {analysis['ticker']}\n\n", "ticker")
        text.insert(tk.END, f"{analysis['title']}\n\n")
        text.insert(tk.END, f"Score: {analysis['score']}/10\n", "score")
        text.insert(tk.END, f"Recommendation: {analysis['recommendation']}\n\n")

        text.insert(tk.END, "PRICES:\n")
        text.insert(tk.END, f"  YES: {analysis['yes_price']:.2%}\n")
        text.insert(tk.END, f"    Bid: {analysis['yes_bid']:.2%}\n")
        text.insert(tk.END, f"    Ask: {analysis['yes_ask']:.2%}\n")
        text.insert(tk.END, f"  NO: {analysis['no_price']:.2%}\n")
        text.insert(tk.END, f"    Bid: {analysis['no_bid']:.2%}\n")
        text.insert(tk.END, f"    Ask: {analysis['no_ask']:.2%}\n\n")

        text.insert(tk.END, "METRICS:\n")
        text.insert(tk.END, f"  Volume: {analysis['volume']:,}\n")
        text.insert(tk.END, f"  Open Interest: {analysis['open_interest']:,}\n")
        text.insert(tk.END, f"  Spread: {analysis['spread']:.2%}\n")
        text.insert(tk.END, f"  Close Time: {analysis['close_time']}\n\n")

        text.insert(tk.END, "ANALYSIS FACTORS:\n")
        for factor in analysis['factors']:
            text.insert(tk.END, f"  • {factor}\n")

        text.config(state=tk.DISABLED)

        # Configure tags
        text.tag_config("ticker", font=("SF Pro Display", 14, "bold"))
        text.tag_config("score", font=("SF Pro Text", 12, "bold"), foreground="#34C759")

    def toggle_auto_refresh(self):
        """Toggle auto-refresh mode"""
        self.auto_refresh = self.auto_refresh_var.get()

        if self.auto_refresh:
            self.schedule_refresh()
        else:
            if self.refresh_timer:
                self.root.after_cancel(self.refresh_timer)
                self.refresh_timer = None

    def schedule_refresh(self):
        """Schedule next refresh"""
        if not self.auto_refresh:
            return

        # Cancel existing timer
        if self.refresh_timer:
            self.root.after_cancel(self.refresh_timer)

        # Schedule next refresh
        interval_ms = self.refresh_interval * 1000
        self.refresh_timer = self.root.after(interval_ms, self.auto_refresh_handler)

    def auto_refresh_handler(self):
        """Handle auto-refresh"""
        if self.auto_refresh and not self.is_analyzing:
            self.start_analysis()
        self.schedule_refresh()

    def update_interval(self, event=None):
        """Update refresh interval"""
        try:
            self.refresh_interval = int(self.interval_var.get())
            if self.auto_refresh:
                self.schedule_refresh()
        except:
            pass

    def update_status(self, message, color):
        """Update status indicator"""
        self.status_label.config(text=f"● {message}", fg=color)

    def open_env_file(self):
        """Open .env file for editing"""
        env_path = os.path.join(os.path.dirname(__file__), '.env')

        if not os.path.exists(env_path):
            # Create from example
            example_path = os.path.join(os.path.dirname(__file__), '.env.example')
            if os.path.exists(example_path):
                import shutil
                shutil.copy(example_path, env_path)

        # Open in default editor
        if sys.platform == 'darwin':  # macOS
            os.system(f'open -t "{env_path}"')
        else:
            messagebox.showinfo("Info", f"Please edit: {env_path}")


def main():
    """Main entry point for macOS app"""
    # Create root window
    root = tk.Tk()

    # Create app
    app = KalshiMacApp(root)

    # Set window icon (if available)
    # root.iconbitmap('icon.icns')  # Uncomment if you have an icon

    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    # Run
    root.mainloop()


if __name__ == '__main__':
    main()
