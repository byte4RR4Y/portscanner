# portscanner
portscanner in python to scan multiple host for specific ports.
It supports multiple threads(standard is 10 threads)


Syntax:
python portsscanner.py [StartIP]-[EndIP] [Port,Port,...] -t [NumberOfThreads}

Example:
python portscanner.py 192.168.0.1-192.168.255.255 135,139,445 -t 100

This will scann all hosts between 192.168.0.1 and 192.168.255.255 and searching for the open ports 135,139,455 with 100 simultanous threads.
