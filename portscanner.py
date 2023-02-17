import argparse
import socket
import threading

def scan_port(ip, port, results):
    try:
        s = socket.socket()
        s.settimeout(0.1)
        s.connect((ip, port))
        s.close()
        results.append(port)
    except:
        pass


def scan_ports(ip_range, ports, num_threads, timeout):
    # Parse the IP range
    start, end = ip_range.split("-")
    start_octets = start.split(".")
    end_octets = end.split(".")
    base_ip = ".".join(start_octets[:3]) + "."

    # Convert the octets to integers
    start_octets = [int(octet) for octet in start_octets]
    end_octets = [int(octet) for octet in end_octets]

    open_ports = {}

    for i in range(start_octets[3], end_octets[3] + 1):
        ip = base_ip + str(i)

        open_ports[ip] = []

        results = []
        threads = []
        for port in ports:
            if "-" in str(port):
                start, end = port.split("-")
                for p in range(int(start), int(end) + 1):
                    t = threading.Thread(target=scan_port, args=(ip, p, results))
                    t.start()
                    threads.append(t)
            else:
                t = threading.Thread(target=scan_port, args=(ip, port, results))
                t.start()
                threads.append(t)

        for t in threads:
            t.join(timeout)

        for port in results:
            open_ports[ip].append(str(port))

    for ip, ports in open_ports.items():
        if len(ports) > 0:
            print(ip + ":", ", ".join(ports))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan for open ports on a range of IP addresses.')
    parser.add_argument("ip_range", help="IP range in the format start-end (e.g. 192.168.0.0-192.168.255.255)")
    parser.add_argument("ports", help="List of ports or ranges of ports to scan (e.g. 22,80,443 or 20-80)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads to use (default is 10)")
    parser.add_argument("-T", "--timeout", type=float, default=0.1, help="Timeout for socket connection in seconds (default is 0.1)")
    args = parser.parse_args()

    # Convert the port list to integers
    ports = args.ports.split(",")
    ports = [port.strip() for port in ports]
    ports = [port for port in ports if port]

    # Scan the ports for each IP address in the range
    scan_ports(args.ip_range, ports, args.threads, args.timeout)
