from datetime import datetime

def log_threat(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ALERT] {timestamp} - {message}")
