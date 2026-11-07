import csv
from pathlib import Path

print("==== SECURITY LOG ANALYZER ====\nWelcome to Security Log Analyzer!")

name = input("What is your name? ").title()
print(f"Welcome, {name}!\n")


def load_logs():
    logs = []
    file_path = Path(__file__).resolve().parent / "login_logs.csv"
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                logs.append(line)
    except FileNotFoundError:
        print("Error: Log file not found.")
    return logs

def get_user_choice():
    option = input("Choose an option: ")
    return option

def show_menu(name):
    print(f"Menu for {name}: ")
    print("1. Analyze log file")
    print("2. Exit")

def analyze_logs(records, threshold = 3):
    success_count = 0
    failed_count = 0
    failed_ips = {}
    print("Analyzing log file...\n")
    for record in records:
        if record["status"] == "failed":
            failed_count += 1
            ip = record["ip"]
            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1
        elif record["status"] == "success":
            success_count += 1
    print("Total login attempts:", len(records))
    print(f"Failed attempts: {failed_count}")
    print(f"Successful attempts: {success_count}")
    print("Failed attempts by IP: ")
    for ip, count in failed_ips.items():
        print(f"{ip}: {count} failed attempts")
    print("\nSecurity Alerts: ")
    suspicious_found = False
    for ip, count in failed_ips.items():
        if count >= threshold:
            suspicious_found = True
            print(f"\n[WARNING] Suspicious activity detected!\n{ip} has failed to log in {count} times")
    if not suspicious_found:
        print("No suspicious activity detected")
    print()
    return failed_ips

while True:
    show_menu(name)
    option = get_user_choice()
    if option == "1":
        records = load_logs()
        if records:
            analyze_logs(records)
    elif option == "2":
        print("Goodbye!")
        break       
    else:
        print("Invalid option. Please choose 1 or 2")