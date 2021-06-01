from socketserver import TCPServer, StreamRequestHandler

from cypher import DiffieHellman


class ServerHandler(StreamRequestHandler):

    def handle(self):
        pass

    def create_public_key(self):
        pass
