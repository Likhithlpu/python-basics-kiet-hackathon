import socket

# Get IP address from domain name
ip_address = socket.gethostbyname('www.kietgroup.com')
print(f"The IP address of www.kietgroup.com is {ip_address}")
