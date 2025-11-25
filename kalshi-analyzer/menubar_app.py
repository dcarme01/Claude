#!/usr/bin/env python3
"""
Kalshi Bet Analyzer - macOS Menu Bar App
Lives in your menu bar for quick access to market analysis
"""

import os
import sys
import threading
import webbrowser
from datetime import datetime
from typing import Optional
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

# Import the analyzer
from analyzer import KalshiAnalyzer

load_dotenv()


class MenuBarApp:
    """macOS menu bar application for Kalshi analysis"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide main window

        # State
        self.analyzer: Optional[KalshiAnalyzer] = None
        self.analyses = []
        self.is_analyzing = False
        self.last_update = None

        # Initialize analyzer
        self.initialize_analyzer()

        # Create menu bar icon using tkinter popup menu
        self.create_menu_bar()

    def initialize_analyzer(self):
        """Initialize the Kalshi analyzer"""
        try:
            demo_mode = os.getenv('KALSHI_DEMO_MODE', 'true').lower() == 'true'
            self.analyzer = KalshiAnalyzer(demo_mode=demo_mode)
        except Exception as e:
            messagebox.showerror("Configuration Error",
                               f"Failed to initialize analyzer: {str(e)}\n\n"
                               "Please check your .env file.")

    def create_menu_bar(self):
        """Create menu bar interface"""
        # Create a simple status window that acts like a menu bar
        self.status_window = tk.Toplevel(self.root)
        self.status_window.title("🎰 Kalshi")

        # Make it stay on top
        self.status_window.attributes('-topmost', True)

        # Position in top-right corner
        screen_width = self.status_window.winfo_screenwidth()
        self.status_window.geometry(f"250x400+{screen_width-270}+30")

        # Create menu content
        frame = tk.Frame(self.status_window, bg='#f5f5f5')
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        title = tk.Label(frame, text="🎰 Kalshi Analyzer",
                        font=("SF Pro Display", 14, "bold"),
                        bg='#f5f5f5')
        title.pack(pady=5)

        # Status
        self.status_label = tk.Label(frame, text="Ready",
                                     font=("SF Pro Text", 10),
                                     bg='#f5f5f5', fg='#666')
        self.status_label.pack()

        # Separator
        tk.Frame(frame, height=1, bg='#ccc').pack(fill=tk.X, pady=10)

        # Analyze button
        tk.Button(frame, text="🔍 Quick Analyze (Top 20)",
                 command=lambda: self.quick_analyze(20),
                 bg='#007AFF', fg='white',
                 font=("SF Pro Text", 11),
                 relief=tk.FLAT, padx=10, pady=5).pack(fill=tk.X, pady=2)

        tk.Button(frame, text="📊 Analyze 50 Markets",
                 command=lambda: self.quick_analyze(50),
                 bg='#007AFF', fg='white',
                 font=("SF Pro Text", 11),
                 relief=tk.FLAT, padx=10, pady=5).pack(fill=tk.X, pady=2)

        tk.Button(frame, text="🔥 Full Analysis (100)",
                 command=lambda: self.quick_analyze(100),
                 bg='#007AFF', fg='white',
                 font=("SF Pro Text", 11),
                 relief=tk.FLAT, padx=10, pady=5).pack(fill=tk.X, pady=2)

        # Separator
        tk.Frame(frame, height=1, bg='#ccc').pack(fill=tk.X, pady=10)

        # Results
        tk.Label(frame, text="Top 3 Opportunities:",
                font=("SF Pro Text", 10, "bold"),
                bg='#f5f5f5').pack(anchor=tk.W)

        self.results_text = tk.Text(frame, height=10, width=30,
                                   font=("SF Mono", 9),
                                   bg='white', relief=tk.FLAT,
                                   wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.results_text.insert(tk.END, "Click analyze to start...")
        self.results_text.config(state=tk.DISABLED)

        # Separator
        tk.Frame(frame, height=1, bg='#ccc').pack(fill=tk.X, pady=10)

        # Actions
        tk.Button(frame, text="📱 Open Full App",
                 command=self.open_full_app,
                 font=("SF Pro Text", 10),
                 relief=tk.FLAT, padx=5, pady=3).pack(fill=tk.X, pady=2)

        tk.Button(frame, text="⚙️ Settings",
                 command=self.open_settings,
                 font=("SF Pro Text", 10),
                 relief=tk.FLAT, padx=5, pady=3).pack(fill=tk.X, pady=2)

        tk.Button(frame, text="❌ Quit",
                 command=self.quit_app,
                 font=("SF Pro Text", 10),
                 relief=tk.FLAT, padx=5, pady=3).pack(fill=tk.X, pady=2)

    def quick_analyze(self, limit):
        """Quick analysis in background"""
        if self.is_analyzing:
            return

        thread = threading.Thread(target=self._analyze, args=(limit,), daemon=True)
        thread.start()

    def _analyze(self, limit):
        """Perform analysis (background thread)"""
        if not self.analyzer:
            self.root.after(0, lambda: messagebox.showerror("Error",
                                                            "Analyzer not initialized"))
            return

        self.is_analyzing = True
        self.root.after(0, lambda: self.status_label.config(text="Analyzing...", fg="#FF9500"))

        try:
            analyses = self.analyzer.analyze_all_markets(limit=limit)
            self.analyses = analyses
            self.last_update = datetime.now()

            # Update display
            self.root.after(0, lambda: self.display_top_results(analyses))
            self.root.after(0, lambda: self.status_label.config(
                text=f"Updated {datetime.now().strftime('%I:%M %p')}", fg="#34C759"))

        except Exception as e:
            self.root.after(0, lambda: self.status_label.config(text="Error", fg="#FF3B30"))
            self.root.after(0, lambda: messagebox.showerror("Analysis Error", str(e)))

        finally:
            self.is_analyzing = False

    def display_top_results(self, analyses):
        """Display top 3 results"""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)

        if not analyses:
            self.results_text.insert(tk.END, "No markets found.")
        else:
            for i, analysis in enumerate(analyses[:3], 1):
                self.results_text.insert(tk.END,
                    f"{i}. {analysis['emoji']} {analysis['ticker']}\n")
                self.results_text.insert(tk.END,
                    f"   Score: {analysis['score']}/10\n")
                self.results_text.insert(tk.END,
                    f"   {analysis['recommendation']}\n")
                self.results_text.insert(tk.END,
                    f"   YES: {analysis['yes_price']:.1%}\n\n")

        self.results_text.config(state=tk.DISABLED)

    def open_full_app(self):
        """Launch full Mac app"""
        import subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.join(script_dir, 'mac_app.py')

        try:
            subprocess.Popen([sys.executable, app_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch app: {e}")

    def open_settings(self):
        """Open settings"""
        env_path = os.path.join(os.path.dirname(__file__), '.env')

        if not os.path.exists(env_path):
            example_path = os.path.join(os.path.dirname(__file__), '.env.example')
            if os.path.exists(example_path):
                import shutil
                shutil.copy(example_path, env_path)

        if sys.platform == 'darwin':
            os.system(f'open -t "{env_path}"')
        else:
            messagebox.showinfo("Settings", f"Edit: {env_path}")

    def quit_app(self):
        """Quit application"""
        self.root.quit()

    def run(self):
        """Run the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    print("🎰 Kalshi Bet Analyzer - Menu Bar App")
    print("Starting menu bar application...")

    app = MenuBarApp()
    app.run()


if __name__ == '__main__':
    main()
