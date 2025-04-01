# 🛡️ Network Threat Monitor (NTM)

A lightweight Python tool that monitors real-time network traffic to detect basic suspicious activity like port scans, blacklisted IPs, and protocol anomalies. Designed for quick deployment and simple visibility into your network.

## ✨ Features
- 📡 Live packet capture via Scapy
- 🚨 Real-time detection of:
  - Port scans
  - Traffic from blacklisted IPs
  - Protocol anomalies (ICMP, ARP flooding, etc.)
- 📟 Terminal alert system with clear logs
- 📁 Optional log file generation for auditing

## ⚙️ Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/ntm.git
cd ntm
```
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Run the monitor:
```bash
sudo python main.py
```
(*Requires root to capture packets on most systems*)

## 🖥️ Usage
You’ll see alerts printed directly to the terminal like:
```
[ALERT] 2025-03-30 23:32:15 - Blacklisted IP detected: 8.8.8.8
[DEBUG] From 10.0.0.19 to port 80
```

Optional logs can be generated for persistent storage by enabling log mode inside the script.

## 📈 Future Plans
- Web dashboard for live visual monitoring
- Export logs to JSON/CSV
- Threat intelligence API integration for IP reputation lookup

## 📄 License
MIT — use freely, modify responsibly.

---

Built for practical experimentation with network monitoring and lightweight IDS concepts.
