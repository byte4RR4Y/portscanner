import argparse
import requests
import threading
from queue import Queue

def scan_port(ip, port, timeout, proxies):
    url = f"http://{ip}:{port}"
    try:
        response = requests.get(url, timeout=timeout, proxies=proxies)
        if response.status_code == 200:
            print(f"{ip}:{port} is open")
    except:
        pass

def scan_ports(q, ports, timeout, proxies):
    while True:
        if q.empty():
            return
        try:
            ip = q.get_nowait()
            for port in ports:
                scan_port(ip, port, timeout, proxies)
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
    parser.add_argument("--proxy", help="Proxy URL (e.g. socks4://proxy.example.com:1080 or http://proxy.example.com:3128)")
    args = parser.parse_args()

    # Convert the IP range to a list of IP addresses
    start_ip, end_ip = args.ip_range.split("-")
    ips = [f"192.168.1.{i}" for i in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1)]

    # Convert the port range to a list of ports
    ports = []
    if "-" in args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
        ports = range(start_port, end_port+1)
    else:
        ports = [int(port) for port in args.ports.split(",")]

    # Set up proxies if provided
    proxies = None
    if args.proxy:
        proxies = {
            "http": args.proxy,
            "https": args.proxy
        }

    # Create a queue with the IP addresses
    q = Queue()
    for ip in ips:
        q.put(ip)

    # Start the worker threads
    for i in range(args.threads):
        t = threading.Thread(target=scan_ports, args=(q, ports, args.timeout, proxies))
        t.daemon = True
        t.start()

    # Wait for all the worker threads to finish
    q.join()
