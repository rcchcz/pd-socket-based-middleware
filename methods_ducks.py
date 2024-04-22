import socket

def method(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # receive api info
        response = client_socket.recv(4096).decode()

        return response
