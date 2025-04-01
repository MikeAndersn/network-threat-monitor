from utils.blacklist import BLACKLISTED_IPS
from src.logger import log_threat

connection_tracker = {}

def analyze_packet(packet):
    print("Received packet:", packet.summary())  # Always log something

    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_port = getattr(packet["IP"], "dport", None)

        print(f"[DEBUG] From {src_ip} to port {dst_port}")

        if src_ip in BLACKLISTED_IPS:
            log_threat(f"Blacklisted IP detected: {src_ip}")

        if dst_port:
            if src_ip not in connection_tracker:
                connection_tracker[src_ip] = set()
            connection_tracker[src_ip].add(dst_port)

            if len(connection_tracker[src_ip]) > 10:
                log_threat(f"Possible port scan from {src_ip} (more than 10 unique ports)")
