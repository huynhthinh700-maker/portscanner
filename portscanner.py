import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    print(f"This is target's ip: {target}")
else:
    print("INVALID FORMAT")
    print("Please enter a right format: python3 portscanner.py <your target>")
    sys.exit()

print("- " * 50)
print("Scanning target .....")
print(f"Time started : {datetime.now()}")
print("- " * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        value = s.connect_ex((target, port))

        if value == 0:
            print(f"[OPEN] Port {port}")
        s.close()

except KeyboardInterrupt:
    print("\nYou've stopped this program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()
