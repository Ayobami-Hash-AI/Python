# TCP Port Scanner — Project Notes

**Source:** [port_scanner.py](../port_scanner.py)  
**Dependency:** Python standard library (`socket`)

## Objective
Practise TCP connection attempts, basic input parsing, and interpreting service reachability.

## Source walkthrough
1. The script prompts for a target hostname/IP and comma-separated port numbers.
2. `get_ports()` parses digit-only entries.
3. `scan_port()` creates an IPv4 TCP socket, sets a two-second timeout, and calls `connect_ex()`.
4. A zero return code prints `OPEN`; nonzero codes print `CLOSED`.

## Run in an authorized lab
```bash
python port_scanner.py
```

Use a host you own or have explicit permission to test.

## Technical limitations
The code does not yet validate port range (1–65535), and a failed connection is **not definitive evidence of a closed port**: filtering, routing, and timeouts can affect results. The script is single-threaded and intended for introductory learning, not production asset discovery.

## Next improvements
Add robust port validation, `with`-based socket cleanup, distinct statuses for connection refusal versus timeout, optional CLI arguments, and unit tests for input parsing.
