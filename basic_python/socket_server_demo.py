import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

print("Server listening on port 12345...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")
    message = "Hello, KIET!"
    client_socket.send(message.encode('utf-8'))
    client_socket.close()
