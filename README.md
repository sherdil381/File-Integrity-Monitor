# Real-Time File Integrity Monitor (FIM)

## Overview
This repository contains a lightweight cybersecurity project that implements a **real-time file integrity monitoring system** in Python. The tool continuously observes specified directories for file creation, modification, or deletion, and generates cryptographic hashes to verify integrity. Events are logged with timestamps, file paths, and hash values to help detect unauthorized or suspicious changes. It can be used for security labs, SOC training, and as a foundation for intrusion detection systems.

---

## Repository structure
- `monitor.py` — main Python script that runs the real-time monitor using `watchdog`.  
- `config.json` — configuration file specifying folders to monitor, hash algorithm, and log file path.  
- `logs.txt` — log file that stores all detected events with timestamps and hashes.  
- `hash_db.json` — local database storing the most recent hash values of monitored files.  
- `README.md` — documentation (this file).  

---

## Features
- Detects **file creation, modification, and deletion** events.  
- Generates **cryptographic hashes** (SHA256 by default, configurable).  
- Monitors one or more folders specified in `config.json`.  
- Logs events with **timestamps and hashes** for auditing.  
- Lightweight, simple, and extendable for alerts or integrations (email, Slack, Discord).  

---

## How to reproduce (Debian/Kali/Ubuntu)
1. Clone the repository:
```bash
git clone https://github.com/sherdil381/file-integrity-monitor.git
cd file-integrity-monitor
```

## Install dependencies in your virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
pip install watchdog
```
## Configure folders, hash algorithm, and log file in config.json:
```
{
    "folders_to_monitor": ["monitor_folder"],
    "hash_algorithm": "sha256",
    "log_file": "logs.txt"
}
  ```
## Create the folder to monitor if it does not exist:

```
mkdir monitor_folder
```

## Run the monitor:
```
python3 monitor.py
```

## Simulate file changes:
```
echo "hello" > monitor_folder/test1.txt      # NEW file
echo "update" >> monitor_folder/test1.txt    # MODIFIED file
rm monitor_folder/test1.txt                  # DELETED file
```

## Planned improvements
```
- Add alerting mechanisms (Slack, Discord, email).

- Add report exports in PDF/HTML format.

- Implement a baseline mode (snapshot + comparison).

Add multi-hash support (MD5, SHA1, SHA256 simultaneously).
```
## Safety & ethics

This project is intended for educational and defensive purposes only. Running it on your own system is safe, but always be cautious when deploying monitoring tools on production environments. Do not use this code for malicious purposes.

Author

--- Made with ❤️ for learning cybersecurity and file monitoring.
GitHub: @sherdil381
 
