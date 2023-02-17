# portscanner
portscanner in python to scan multiple hosts for specific ports.
It supports multiple threading (standard is 10 threads)


Syntax:
python portsscanner.py [StartIP]-[EndIP] [Port,Port,... or Port-Port] -t [NumberOfThreads}

Example:
python portscanner.py 192.168.0.1-192.168.255.255 135,139,445 -t 100
python portscanner.py 192.168.0.1-192.168.255.255 1-65535

for help type:
python portscanner.py -h 
