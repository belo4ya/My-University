import time
from socketserver import TCPServer, StreamRequestHandler
from cypher import DiffieHellman


class ClientApp(StreamRequestHandler):

    def handle(self):
        pass

    def create_public_key(self):
        pass
