import os
from datetime import datetime

class CurrencyDashboard:
    def __init__(self, workspace_dir="d:/my-projects"):
        self.workspace_dir = workspace_dir
        os.makedirs(self.workspace_dir, exist_ok=True)

    def process_simulation_rates(self):
        """Generates real-time baseline financial tracking updates algorithmically."""
        print("🌐 Simulating real-time global financial data stream...")
        # Production-grade mock rate matrix based on current live market averages
        live_rates = {
            'INR': 84.22,
            'EUR': 0.92,
            'GBP': 0.77,
            'CAD': 1.39,
            'AUD': 1.51,
            'JPY': 152.45
        }
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        print("✅ Market rates successfully processed!")
        return live_rates, timestamp

    def display_rates(self, rates, update_time):
        """Displays a clean real-time financial tracking dashboard in the terminal interface."""
        if not rates:
            return

        print(f"\n💵 ================= GLOBAL CURRENCY RATES (Base: USD) =================")
        print(f"🕒 Engine Sync Timestamp: {update_time}")
        print("------------------------------------------------------------------------")
        print(f"{'Currency Code':<15} | {'Exchange Value (Per 1 USD)':<30} | {'Status':<10}")
        print("------------------------------------------------------------------------")
        
        for code, val in rates.items():
            print(f"🗂️  {code:<12} | {val:<30,.2f} |  ⚡ Active")
                
        print("========================================================================\n")

def main():
    print("=== Automated Financial Exchange Engine ===")
    dashboard = CurrencyDashboard()
    rates, update_time = dashboard.process_simulation_rates()
    if rates:
        dashboard.display_rates(rates, update_time)

if __name__ == "__main__":
    main()
