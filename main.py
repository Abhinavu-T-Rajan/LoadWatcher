#!/usr/bin/env python3
import psutil
import requests
import time

# 🚨 Set your webhook URL here (e.g. Discord, Slack, or your own endpoint)
WEBHOOK_URL = "https://your-webhook-url-here"

# 🔧 Thresholds (change as needed)
CPU_THRESHOLD = 85  # in percent
MEM_THRESHOLD = 90  # in percent
DISK_THRESHOLD = 90  # in percent

def send_alert(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(f"[!] Failed to send webhook: {e}")

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu > CPU_THRESHOLD:
            send_alert(f"⚠️ High CPU Usage: {cpu}%")
        if mem > MEM_THRESHOLD:
            send_alert(f"⚠️ High Memory Usage: {mem}%")
        if disk > DISK_THRESHOLD:
            send_alert(f"⚠️ High Disk Usage: {disk}%")

        time.sleep(60)  # check every 60 seconds (Change it upto your wish)

if __name__ == "__main__":
    monitor()
