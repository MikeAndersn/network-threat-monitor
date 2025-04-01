from scapy.all import sniff
from src.analyzer import analyze_packet

def sniff_packets():
    print("[*] Starting packet sniffer...")
    sniff(prn=analyze_packet, store=False)
