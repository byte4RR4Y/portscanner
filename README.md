# portscanner
portscanner in python to scan multiple hosts for specific ports.
It supports multiple threading (default is 10 threads)

![portscanner](https://user-images.githubusercontent.com/121404035/219864809-429c7b22-69dc-4f1e-b717-3ae90493836e.png)
Example:

python portscanner.py 192.168.0.0-192.168.255.255 22,23,80,443 -t 100

python portscanner.py 192.168.0.0-192.168.255.255 1-1024 -t 200
