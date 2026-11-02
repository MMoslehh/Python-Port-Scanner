import socket

target = "127.0.0.1"
ports = [21, 22, 80, 443, 3306, 8080]

print("Scanning", target)
print("------------------------")

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed or filtered")

    scanner.close()

print("------------------------")
print("Scan completed.")