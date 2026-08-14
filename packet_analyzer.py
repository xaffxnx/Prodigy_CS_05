"""
Task-05 : Network Packet Analyzer (Educational Demo)
Prodigy InfoTech - Cyber Security Internship

Description:
A simple packet sniffer that captures live network packets on your
own machine/network and displays key information: source/destination
IP addresses, protocol, and a preview of the payload.

IMPORTANT - Ethical Use Notice:
- This tool must ONLY be run on networks/systems you own or have
  explicit written permission to monitor.
- Capturing traffic on a network without authorization is illegal
  in most jurisdictions (e.g. unauthorized access laws).
- This script is for learning how packet sniffing / protocol
  analysis works, not for intercepting other people's data.
- Requires administrator/root privileges to run (raw socket access).

Dependency:
    pip install scapy
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

LOG_FILE = "packet_log.txt"


def write_log(line: str):
    """Append a line to the log file and print it to console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {line}"
    print(entry)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def get_protocol_name(packet) -> str:
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def process_packet(packet):
    """Callback executed for every captured packet."""
    if not packet.haslayer(IP):
        return  # skip non-IP packets (e.g. ARP)

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    proto = get_protocol_name(packet)

    line = f"SRC: {src_ip:15}  ->  DST: {dst_ip:15}  | Protocol: {proto}"

    # Add port info if TCP/UDP
    if packet.haslayer(TCP):
        line += f"  | SPort: {packet[TCP].sport}  DPort: {packet[TCP].dport}"
    elif packet.haslayer(UDP):
        line += f"  | SPort: {packet[UDP].sport}  DPort: {packet[UDP].dport}"

    # Show a short preview of the payload (if any), safely decoded
    if packet.haslayer(Raw):
        try:
            payload = bytes(packet[Raw].load)
            preview = payload[:40].decode(errors="replace")
            line += f"  | Payload preview: {preview!r}"
        except Exception:
            pass

    write_log(line)


def main():
    print("=== Network Packet Analyzer (Task-05) ===")
    print("Prodigy InfoTech - Cyber Security Internship")
    print("Educational use only. Run only on networks you own or are authorized to monitor.\n")
    print("Starting capture... Press Ctrl+C to stop.\n")

    try:
        # count=0 means capture indefinitely until Ctrl+C
        sniff(prn=process_packet, store=False, count=0)
    except PermissionError:
        print("\nERROR: Permission denied. Run this script as Administrator (Windows) or with sudo (Linux/Mac).")
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")


if __name__ == "__main__":
    main()
