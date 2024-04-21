import socket
import requests

def get_color_info(color):
    url = f'http://www.thecolorapi.com/id?format=json&hex={color}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Failed to fetch color information. {response.status_code}'}

def main():
    host = 'localhost'
    port = 5555

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f'Colori server listening on {host}:{port}.')

        while True:
            client_socket, address = server_socket.accept()
            print(f'Connection from {address} established.')

            color = client_socket.recv(1024).decode().strip()
            color_info = get_color_info(color)

            response = str(color_info).encode()
            client_socket.sendall(response)

            client_socket.close()

if __name__ == '__main__':
    main()
