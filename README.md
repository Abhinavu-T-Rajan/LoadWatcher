# 🖥️ LoadWatcher

**LoadWatcher** is a lightweight Python-based system resource monitoring tool that sends **webhook alerts** when your Linux system is under heavy load.

Useful for servers, homelabs, or pentest boxes that need to notify you (via Discord, Slack, or custom webhooks) when things go wrong.

---

## 🚀 Features

- ✅ Monitors **CPU**, **RAM**, and **Disk** usage
- 📡 Sends **webhook alerts** when thresholds are exceeded
- 🪶 Runs as a **minimal systemd service**
- ⚙️ Customizable thresholds and alerting
- 🐧 Built for Linux systems

---

## 📦 Requirements

- Python 3
- `psutil` and `requests` libraries

Install with:

```bash
sudo apt install python3 python3-pip
pip3 install psutil requests
```

# Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Abhinavu-T-Rajan/LoadWatcher.git
cd LoadWatcher
```

### 2. Configure your webhook

```bash
nano loadwatcher.py
```

```python
WEBHOOK_URL = "https://your-webhook-url-here"
```

### Make it executable

```bash
chmod +x loadwatcher.py
```
**(Optional) Move to a global path:**

```bash
sudo cp loadwatcher.py /usr/local/bin/loadwatcher
```
# Create a systemd service

```bash
sudo nano /etc/systemd/system/loadwatcher.service
```
then

```service
[Unit]
Description=LoadWatcher - System Resource Webhook Monitor
After=network.target

[Service]
ExecStart=/usr/bin/python3 /usr/local/bin/loadwatcher
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

### Enable & start

```bash
sudo systemctl daemon-reload
sudo systemctl enable loadwatcher
sudo systemctl start loadwatcher
```

### Check status

```bash
sudo systemctl status loadwatcher

```
