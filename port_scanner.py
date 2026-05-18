import socket


def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        sock.close()

    except socket.gaierror:
        print("Invalid target IP address or hostname.")
    except socket.error as error:
        print(f"Network error: {error}")


def get_ports(port_input):
    ports = []

    for item in port_input.split(","):
        item = item.strip()

        if item.isdigit():
            ports.append(int(item))
        else:
            print(f"Invalid port ignored: {item}")

    return ports


target = input("Enter target IP address: ")
port_input = input("Enter ports to scan, separated by commas: ")

ports = get_ports(port_input)

if not ports:
    print("No valid ports entered.")
else:
    print(f"\nScanning target: {target}\n")

    for port in ports:
        scan_port(target, port)