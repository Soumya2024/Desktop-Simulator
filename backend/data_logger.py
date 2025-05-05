import csv
from datetime import datetime

def log_event(device, state):
    with open("data/logs/usage_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), device, state])
