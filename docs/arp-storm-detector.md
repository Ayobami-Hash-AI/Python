# ARP Storm Detector — Project Notes

**Source:** [arp_storm_detector.py](../arp_storm_detector.py)  
**Input:** [arp.pcap](../arp.pcap)  
**Dependency:** Scapy (`pip install scapy`)

## Objective
Read a packet capture, isolate ARP request frames, estimate request frequency, and flag unusually high rates based on a configurable threshold.

## Implementation observed in the source
1. `rdpcap()` loads packets from the local `arp.pcap` file.
2. `filter_arp_requests()` selects packets where `ARP.op == 1`.
3. `calculate_arp_request_rate()` divides the number of requests by the time between the first and last matching packet.
4. `detect_arp_storm()` compares that rate to a default threshold of **20 requests per second**.
5. If the threshold is exceeded, `print_summary()` reports request count and unique source MAC/IP counts.

## How to run
```bash
python -m pip install scapy
python arp_storm_detector.py
```

Run from the repository root with `arp.pcap` present.

## Interpretation and limitations
This is an introductory heuristic, **not a validated intrusion detection system**. Its result depends on capture completeness, packet ordering, the selected threshold, and the time window. A high ARP rate can have benign explanations; it does not by itself prove an attack. No benchmark, test suite, or verified output is claimed here.

## Next engineering improvements
Add command-line file selection, bounded time windows, input/error handling, reproducible tests, and sample output generated from a reviewed capture.

**Ethical scope:** Use authorized packet captures only.
