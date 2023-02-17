#! /usr/bin/env/python

import argparse
import socket
import struct

def ip_range(start_ip, end_ip):
    # Convert the IP addresses to integers
    start = struct.unpack('>I', socket.inet_aton(start_ip))[0]
    end = struct.unpack('>I', socket.inet_aton(end_ip))[0]

    # Loop over the IP addresses in the range
    for ip in range(start, end + 1):
        yield socket.inet_ntoa(struct.pack('>I', ip))

def scan_ports(ip_range, ports):
    for ip in ip_range:
        open_ports = []
        for port in ports:
            try:
                s = socket.socket()
                s.settimeout(0.1)
                s.connect((ip, port))
                open_ports.append(str(port))
                s.close()
            except:
                pass
        if len(open_ports) > 0:
            print(ip + ":", ", ".join(open_ports))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_range", help="IP range in the format start-end")
    parser.add_argument("ports", help="Comma separated list of ports to scan")
    args = parser.parse_args()

    # Convert the IP range to a list of IP addresses
    start_ip, end_ip = args.ip_range.split("-")
    ips = ip_range(start_ip, end_ip)

    # Convert the port list to integers
    ports = [int(port) for port in args.ports.split(",")]

    # Scan the ports for each IP address in the range
    scan_ports(ips, ports)
