import socket

def method(host, port):
    color = input('Enter a color in hexadecimal format (e.g., FF0000 for red or 000000 for black.): ')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # send the color to the server
        client_socket.sendall(color.encode())

        # receive api info
        response = client_socket.recv(4096).decode()

        return response
