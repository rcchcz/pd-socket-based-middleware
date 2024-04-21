import socket
import pickle

services = {
    'colori': {
        'url': 'localhost',
        'port': 5555,
        'lib': 'methods_colori'
    },
}

class ClientStub:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.host = ''
        self.port = ''
        self.lib: ''

    def resolve_server_info(self):
        if self.service_name in services:
            service_info = services[self.service_name]
            self.host = service_info['url']
            self.port = service_info['port']
            self.lib = service_info['lib']
        else:
            raise ValueError(f'Service {self.service_name} not found in services database.')

    def __str__(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        host = 'localhost'
        port = 3000
        server_socket.bind((host, 3000))

        server_socket.listen(1)
        print(f'DNS middleware listening on {host}:{port}.')

        while True:
            # waiting connection
            client_socket, address = server_socket.accept()
            print(f'Connection from {address}.')

            serialized_stub = client_socket.recv(4096)
            client_stub = pickle.loads(serialized_stub)

            if client_stub.service_name in services:
                service_info = services[client_stub.service_name]
                client_stub.host = service_info['url']
                client_stub.port = service_info['port']
                client_stub.lib = service_info['lib']
            else:
                raise ValueError(f'Service {client_stub.service_name} not found in services database.')

            serialized_stub_response = pickle.dumps(client_stub)
            client_socket.sendall(serialized_stub_response)

            client_socket.close()


if __name__ == '__main__':
    main()
