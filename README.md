# portscanner
portscanner in python to scan multiple hosts for specific ports.
It supports multiple threading (default is 10 threads)

Files:

--------------------------------------------------------------------------------

portscanner.py =  portscanner in python(the fastest version)
                  Updated: Connection timeout error solved, added socks5 proxy connection

portscanner.exe = portscanner as Windows executable(not up to date)

portscanner =     portscanner as Linux executable
                  Updated: Connection timeout error solved, added socks5 proxy connection

![Screenshot_2023-02-20_17-20-38](https://user-images.githubusercontent.com/121404035/220157785-d7a31c0a-608d-47ba-8fec-a532e69fc696.png)


Example:
--------------------------------------------------------------------------------

python3 portscanner.py 192.168.0.0-192.168.255.255 22,23,80,443 -t 100

python3 portscanner.py 192.168.0.0-192.168.255.255 1-1024 -t 200 -T 0.5

python3 portscanner.py 2.161.0.0-2.175.255.255 80 -t 200 -T 5.0 --proxy socks5://184.168.122.103:7890
--------------------------------------------------------------------------------

