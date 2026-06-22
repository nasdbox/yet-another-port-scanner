import socket
import sys
from datetime import datetime

target_host = input("Enter target IP or hostname: ")

try:
    # Convert hostname to IP address
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n[!] Hostname could not be resolved.")
    sys.exit()

print("-" * 50)
print(f"Scanning: {target_ip}")
print(f"Started:  {datetime.now()}")
print("-" * 50)

try:
    # Scan common ports from 1 to 1024
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # Prevent the script from hanging
        
        # connect_ex returns 0 if the port is open
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan stopped by user.")
    sys.exit()
except socket.error:
    print("\n[!] Connection error.")
    sys.exit()
