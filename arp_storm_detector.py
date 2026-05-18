from scapy.all import rdpcap, ARP


# Read pcap file
def read_pcap(file_name):
    packets = rdpcap(file_name)
    return packets


# Filter only ARP request packets
def filter_arp_requests(packets):
    arp_requests = []

    for packet in packets:
        if packet.haslayer(ARP):
            if packet[ARP].op == 1:  # ARP Request
                arp_requests.append(packet)

    return arp_requests


# Calculate ARP request rate
def calculate_arp_request_rate(arp_requests):
    if len(arp_requests) < 2:
        return 0

    start_time = arp_requests[0].time
    end_time = arp_requests[-1].time

    duration = end_time - start_time

    if duration == 0:
        return 0

    rate = len(arp_requests) / duration
    return rate


# Detect ARP storm
def detect_arp_storm(arp_requests, threshold=20):
    rate = calculate_arp_request_rate(arp_requests)

    if rate > threshold:
        return True, rate
    else:
        return False, rate


# Print summary
def print_summary(arp_requests):
    source_macs = set()
    source_ips = set()

    for packet in arp_requests:
        source_macs.add(packet.hwsrc)
        source_ips.add(packet.psrc)

    print("\n===== ARP STORM SUMMARY =====")
    print(f"Total ARP Requests: {len(arp_requests)}")
    print(f"Unique Source MAC Addresses: {len(source_macs)}")
    print(f"Unique Source IP Addresses: {len(source_ips)}")


# Main program
pcap_file = "arp.pcap"

packets = read_pcap(pcap_file)

arp_requests = filter_arp_requests(packets)

storm_detected, rate = detect_arp_storm(arp_requests)

print(f"ARP Request Rate: {rate:.2f} requests/second")

if storm_detected:
    print("\n⚠ ARP Storm Detected!")
    print_summary(arp_requests)
else:
    print("\nNo ARP Storm Detected.")