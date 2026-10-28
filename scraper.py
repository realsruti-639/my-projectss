import csv
import os
from datetime import datetime

class LogAnalyzerEngine:
    def __init__(self, workspace_dir="d:/my-projects"):
        self.workspace_dir = workspace_dir
        self.mock_log_file = os.path.join(self.workspace_dir, "server_access.log")
        self.output_report = os.path.join(self.workspace_dir, "security_incident_report.csv")
        os.makedirs(self.workspace_dir, exist_ok=True)
        
    def generate_mock_logs(self):
        """Generates raw system access logs locally to simulate a data pipeline source."""
        print("📝 Preparing raw local system log streams...")
        logs = [
            "2026-10-28 10:15:32 | IP: 192.168.1.45 | STATUS: 200 | REQ: GET /api/v1/login | USER: sruti_dev",
            "2026-10-28 10:17:11 | IP: 45.22.89.102 | STATUS: 403 | REQ: POST /admin/db | USER: anonymous_attacker",
            "2026-10-28 10:20:05 | IP: 192.168.1.12 | STATUS: 200 | REQ: GET /index.html | USER: guest_user",
            "2026-10-28 10:22:44 | IP: 185.40.11.23 | STATUS: 403 | REQ: GET /config.json | USER: unknown_bot",
            "2026-10-28 10:25:19 | IP: 192.168.1.45 | STATUS: 500 | REQ: POST /api/v1/upload | USER: sruti_dev",
            "2026-10-28 10:28:01 | IP: 91.210.50.4  | STATUS: 403 | REQ: POST /wp-login.php | USER: malicious_crawler"
        ]
        with open(self.mock_log_file, mode='w', encoding='utf-8') as file:
            for log in logs:
                file.write(log + "\n")
        print("✅ Raw source log files prepared locally on D drive!")

    def analyze_and_compile_report(self):
        """Scans the local log files, filters out security threats (403 errors), and builds a CSV report."""
        if not os.path.exists(self.mock_log_file):
            print("❌ Source data stream missing.")
            return

        print("📊 Scanning data matrix for security incidents (HTTP 403)...")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        incidents_found = []

        # Parse local text files natively
        with open(self.mock_log_file, mode='r', encoding='utf-8') as file:
            for line in file:
                if "STATUS: 403" in line:
                    parts = [part.strip() for part in line.split("|")]
                    log_time = parts[0]
                    ip_addr = parts[1].replace("IP: ", "")
                    req_path = parts[3].replace("REQ: ", "")
                    username = parts[4].replace("USER: ", "")
                    incidents_found.append([log_time, ip_addr, req_path, username])

        # Write clean, structured data matrix
        with open(self.output_report, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Security Audit Summary Generated:", timestamp, "", ""])
            writer.writerow(["Timestamp", "Source IP Address", "Attempted Target Resource", "Flagged Username Identity"])
            for incident in incidents_found:
                writer.writerow(incident)

        print(f"💾 Automated security compilation complete! Report saved: {self.output_report}")
        return incidents_found

    def display_incident_dashboard(self, incidents):
        """Prints a clean data breakdown directly inside the terminal interface."""
        if not incidents:
            print("📊 Analysis Complete: Zero security anomalies flagged.")
            return

        print("\n🚨 ================= SECURITY INCIDENT DETECTED HEADS-UP =================")
        print(f"{'Incident Timestamp':<20} | {'Attacker IP':<15} | {'Target Resource Path':<22} | {'Identity':<15}")
        print("--------------------------------------------------------------------------------")
        for item in incidents:
            print(f"{item[0]:<20} | {item[1]:<15} | {item[2]:<22} | {item[3]:<15}")
        print("==================================================================================\n")

def main():
    print("=== System Automation & Analytical Log Engine ===")
    analyzer = LogAnalyzerEngine()
    analyzer.generate_mock_logs()
    flagged_events = analyzer.analyze_and_compile_report()
    analyzer.display_incident_dashboard(flagged_events)

if __name__ == "__main__":
    main()
