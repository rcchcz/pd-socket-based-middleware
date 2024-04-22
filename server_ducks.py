import socket
import requests

def get_duck_image():
    url = f'https://random-d.uk/api/v2/quack'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Failed to fetch duck image. {response.status_code}'}

def main():
    host = 'localhost'
    port = 6666

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f'Ducks server listening on {host}:{port}.')

        while True:
            client_socket, address = server_socket.accept()
            print(f'Connection from {address} established.')

            duck_image = get_duck_image()

            response = str(duck_image).encode()
            client_socket.sendall(response)

            client_socket.close()

if __name__ == '__main__':
    main()
