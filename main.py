import sys
import socket
import pickle
from dns import ClientStub

def import_lib(lib_name):
    lib = __import__(lib_name)
    return lib

def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <service_name>')
        return

    service_name = sys.argv[1]

    try:
        client_stub = ClientStub(service_name)
        serialized_stub = pickle.dumps(client_stub)

        # connect to dns middleware
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dns_socket:
            dns_socket.connect(('localhost', 3000))
            dns_socket.sendall(serialized_stub)
            print('ClientStub sent to DNS middleware.')

            # updated ClientStub from dns
            serialized_response = dns_socket.recv(4096)
            updated_stub = pickle.loads(serialized_response)

            updated_stub.__str__()

            # import lib and call the available method
            library = import_lib(updated_stub.lib)
            response = library.method(updated_stub.host, updated_stub.port)
            print(f' \n {response} \n')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
