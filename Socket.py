# import socket

# connec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connec.connect(("google.com", 80))
# connec.send(b"GET / HTTP/1.1 \r\n")
# connec.send(b"HOST: www.google.com \r\n")
# connec.send(b"connection: close \r\n")
# connec.send(b"\r\n")

# result = connec.recv(1024)
# print(result)


import socket

target = "scanme.nmap.org"
target_ip = socket.gethostbyname(target)

print(f"Scanning {target}...")

# Loop through ports 1 to 1024
for port in range(1, 1025):
    # Create the socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Short timeout to make it move faster
    
    # Check the connection
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"Port {port} is open")
        
    s.close()

print("Scan finished.")