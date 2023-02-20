# portscanner
portscanner in python to scan multiple hosts for specific ports.
It supports multiple threading (default is 10 threads)

Files:

portscanner.py = portscanner in python(the fastest version)

potrscanner.new.py = portscanner in python SUPPORTS PROXY CONNECTION (http, https, socks4, socks5)but shows filtered ports too.

portscanner.exe = portscanner as Windows executable(not up to date)

portscanner = portscanner as Linux executable

![portscanner](https://user-images.githubusercontent.com/121404035/219865746-b3d634e7-47f5-4e8f-a490-244c69cb460c.png)


Example:

python portscanner.py 192.168.0.0-192.168.255.255 22,23,80,443 -t 100

python portscanner.py 192.168.0.0-192.168.255.255 1-1024 -t 200 -T 0.5

--------------------------------------------------------------------------------

portscanner.new.py:

![Screenshot_2023-02-19_14-34-19](https://user-images.githubusercontent.com/121404035/219952199-5bea0213-da70-4d96-9f86-30455eb4eb27.png)

Example:

python portscanner.py 192.168.0.0-192.168.255.255 1-1024 -t 200 -T 2.0 --proxy socks5://127.0.0.1:9050
