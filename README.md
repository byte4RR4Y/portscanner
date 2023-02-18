# portscanner
portscanner in python to scan multiple hosts for specific ports.
It supports multiple threading (default is 10 threads)
and you can set the timeout with -T flag in seconds (default is 0.1)


Syntax:
python portsscanner.py [StartIP]-[EndIP] [Port,Port,... or Port-Port] -t [NumberOfThreads]

Example:
python portscanner.py -h                          

python portscanner.py 192.168.0.1-192.168.255.255 135,139,445 -t 100

python portscanner.py 192.168.0.1-192.168.255.255 1-65535 -t 500
