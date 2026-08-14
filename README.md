# Prodigy_CS_05 — Network Packet Analyzer (Educational Demo)

## 📡 Task-05 | Prodigy InfoTech — Cyber Security Internship

A Python-based packet sniffer that captures live network traffic and displays key information: source/destination IP addresses, protocol (TCP/UDP/ICMP), port numbers, and a payload preview — built using the Scapy library.

## ⚠️ Ethical Use Notice

This tool was built strictly for educational purposes to understand how network packet capture and protocol analysis work, as part of a cybersecurity internship curriculum.

- This tool must **ONLY** be run on networks/systems you own or have explicit permission to monitor.
- Capturing traffic on a network without authorization is **illegal** in most jurisdictions.
- This project should only be used in a controlled, authorized environment for learning purposes.
- Encrypted traffic (HTTPS/TLS) will show unreadable/encrypted payload bytes by design — this tool does not decrypt or break encryption in any way.

## 📋 Features

- Live packet capture on the local network interface
- Displays source IP, destination IP, and protocol for every packet
- Shows source/destination ports for TCP and UDP packets
- Attempts to preview readable payload data (when unencrypted)
- Logs every captured packet with a timestamp to a local file (`packet_log.txt`)
- Clean console output while capturing, stoppable anytime with `Ctrl+C`

## 🛠️ Tech Stack

- **Language:** Python 3
- **Library used:** [Scapy](https://scapy.net/) — for packet capture and parsing
- **OS dependency (Windows only):** [Npcap](https://npcap.com/) — required driver for raw packet capture

## 🚀 How to Set Up & Run

1. Install Npcap (Windows only) from npcap.com — during install, enable **"WinPcap API-compatible mode"**.
2. Install Scapy:
   ```
   pip install scapy
   ```
3. Clone this repository:
   ```
   git clone https://github.com/xaffxnx/Prodigy_CS_05.git
   ```
4. Navigate to the project folder:
   ```
   cd Prodigy_CS_05
   ```
5. Run the script **as Administrator** (Windows) or with `sudo` (Linux/Mac) — raw socket access requires elevated privileges:
   ```
   python packet_analyzer.py
   ```
6. Generate some traffic (browse a website, stream a video) to see live packets being captured.
7. Press `Ctrl+C` to stop the capture.

## 📊 Sample Output

```
[2026-08-14 11:46:58] SRC: 192.168.0.1      ->  DST: 192.168.0.102   | Protocol: TCP | SPort: 1900  DPort: 61188 | Payload preview: 'HTTP/1.1 200 OK\r\nContent-Type: text/xml;'
[2026-08-14 11:52:29] SRC: 172.217.194.119  ->  DST: 192.168.0.102   | Protocol: TCP | SPort: 443   DPort: 55634 | Payload preview: '\x17\x03\x03\x01b...' (encrypted TLS data)
```

Note how HTTPS/TLS traffic shows encrypted, unreadable bytes — this is expected behavior and demonstrates why encryption protects data even when packets are intercepted.

## 📖 What I Learned

- How raw packet capture works at the OS/network interface level
- The structure of IP, TCP, and UDP headers
- The difference between plaintext protocols (like UPnP/SSDP) and encrypted protocols (like HTTPS/TLS) at the packet level
- Why encryption is critical for protecting data in transit, even from someone with local network visibility
- Responsible, authorized use of network analysis tools in cybersecurity

## 👤 Author

**Sunesra Affan Salauddin**
Cybersecurity Enthusiast | VAPT | CEH v13 Trained
[LinkedIn](https://linkedin.com/in/affan-sunesra-a5a470286)

---
*Built as part of the Cyber Security Internship at Prodigy InfoTech.*
