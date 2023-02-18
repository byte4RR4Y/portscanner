import argparse
import socket
import struct
import threading
from queue import Queue

def ip_range(start_ip, end_ip):
    # Convert the IP addresses to integers
    start = struct.unpack('>I', socket.inet_aton(start_ip))[0]
    end = struct.unpack('>I', socket.inet_aton(end_ip))[0]

    # Loop over the IP addresses in the range
    for ip in range(start, end + 1):
        yield socket.inet_ntoa(struct.pack('>I', ip))

def scan_ports(q, ports, timeout):
    while True:
        if q.empty():
            return
        try:
            ip = q.get_nowait()
            open_ports = []
            for port in ports:
                try:
                    s = socket.socket()
                    s.settimeout(timeout)
                    s.connect((ip, port))
                    open_ports.append(str(port))
                    s.close()
                except:
                    pass
            if len(open_ports) > 0:
                print(ip + ":", ", ".join(open_ports))
        except Queue.Empty:
            break
        finally:
            q.task_done()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_range", help="IP range in the format start-end (e.g. 192.168.0.0-192.168.255.255)")
    parser.add_argument("ports", help="Port range (e.g. 1-1024) or comma separated list of ports (e.g. 22,80,443)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default 10)")
    parser.add_argument("-T", "--timeout", type=float, default=1.0, help="Connection timeout in seconds (default 1.0)")
    args = parser.parse_args()

    # Convert the IP range to a list of IP addresses
    start_ip, end_ip = args.ip_range.split("-")
    ips = list(ip_range(start_ip, end_ip))

    # Convert the port range to a list of ports
    ports = []
    if "-" in args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
        ports = range(start_port, end_port+1)
    else:
        ports = [int(port) for port in args.ports.split(",")]

    # Create a queue with the IP addresses
    q = Queue()
    for ip in ips:
        q.put(ip)

    # Start the worker threads
    for i in range(args.threads):
        t = threading.Thread(target=scan_ports, args=(q, ports, args.timeout))
        t.daemon = True
        t.start()

    # Wait for all the worker threads to finish
    q.join()
