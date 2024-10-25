import socket

class SocketHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def bind_and_listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def accept(self):
        return self.socket.accept()

    def send(self, data):
        self.socket.send(data)

    def recv(self, bufsize):
        return self.socket.recv(bufsize)

    def close(self):
        if self.socket:
            self.socket.close()