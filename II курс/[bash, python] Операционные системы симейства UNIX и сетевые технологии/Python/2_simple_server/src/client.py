import socket

from src.package import Package


def client(host, port):
    message = Package(
        headers={
            "encoding": "utf-8",
            "username": "admin",
            "password": "admin"
        },
        content="Hello, world!"
    )
    # message.cookies = {"session-token": "",
    #                    "session-start": ""},

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.connect(("localhost", 40096))
        sock.sendall(message.to_bytes())
        response = Package.from_bytes(sock.recv(4096))

        # print(f"Received: {response}")
        print(f"Received:\n{response.content}")


if __name__ == '__main__':
    host, port = "localhost", 8899
    client(host, port)
