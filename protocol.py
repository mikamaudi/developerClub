class Protocol:
    @staticmethod
    def __init__(self, connection):
        self.connection = connection

    @staticmethod
    def send_key(self, key_char):
        self.connection.sendall(key_char.encode('utf-8'))

    @staticmethod
    def receive_key(self):
        data = self.connection.recv(1024)
        if data:
            return data.decode('utf-8')
        return None
