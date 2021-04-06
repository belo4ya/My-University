import socket

from src.package import Package

MESSAGE_AUTH = Package(
    headers={
        "encoding": "utf-8",
        "username": "admin",
        "password": "admin"
    },
    content="Hello, world!"
)
MESSAGE_SESSION = Package(
    headers={
        "encoding": "utf-8",
        "username": "admin"
    },
    cookies={
        "session-token": "b501144b-c985-48af-8e8e-6be8ec05e11b",
    },
    content="Hello, world!"
)
MESSAGE_SHUTDOWN = Package(
    headers={
        "encoding": "utf-8",
        "username": "admin",
        "execute": "/shutdown"
    },
    cookies={
        "session-token": "b501144b-c985-48af-8e8e-6be8ec05e11b",
    },
    content="Empty body"
)

message = MESSAGE_SHUTDOWN


def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.connect(("localhost", 40096))
        sock.sendall(message.to_bytes())
        response = Package.from_bytes(sock.recv(4096))

        print(f"Received:")
        print(f"status: {response.status}")
        print(f"headers: {response.headers}")
        print(f"cookies: {response.cookies}")
        print("content " + "=" * 62)
        print(response.content)
        print("=" * 70 + "\n")


if __name__ == '__main__':
    host, port = "localhost", 8899
    client(host, port)
