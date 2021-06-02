import random
import argparse

from src.server import Server, Handler
from src.client import client

parser = argparse.ArgumentParser()
parser.add_argument("cmd", type=str, help="runserver or runclient")
parser.add_argument("--host", type=str, help="any hostname, default: localhost")
parser.add_argument("--port", type=int, help="port number")
args = parser.parse_args()


def run_server(host="localhost", port=40096):
    with Server((host, port), Handler) as server:
        server.serve_forever()


def run_client(host, port=9991):
    client(host, port)


if __name__ == '__main__':
    host = args.host or "localhost"
    port = args.port or random.randint(10_000, 32_000)

    if args.cmd == "runserver":
        host = "localhost"
        port = 40096
        run_server(host, port)
    if args.cmd == "runclient":
        run_client(host, port)
