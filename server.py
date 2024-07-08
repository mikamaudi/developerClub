import socket
from pynput import keyboard
from protocol import Protocol


class KeyPressServer:
    def __init__(self, host='0.0.0.0', port=80):
        self.server_address = (host, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(1)
        self.protocol = None
        print(f"Server listening on {host}:{port}")

    def on_press(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        if self.protocol:
            self.protocol.send_key(key_char)

    def start(self):
        self.connection, self.client_address = self.server_socket.accept()
        self.protocol = Protocol(self.connection)
        print(f"Connection from {self.client_address}")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def close(self):
        self.connection.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = KeyPressServer()
    try:
        server.start()
    finally:
        server.close()
