import socket
from protocol import Protocol


class KeyPressClient:
    def __init__(self, host='192.168.0.117', port=80):
        self.server_address = (host, port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)
        self.protocol = Protocol(self.client_socket)
        print(f"Connected to server {host}:{port}")

    def listen_for_keys(self):
        try:
            while True:
                key_char = self.protocol.receive_key()
                if key_char:
                    print(key_char, end=" ")

                else:
                    break
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    client = KeyPressClient()
    client.listen_for_keys()
