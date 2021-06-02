import datetime
import hashlib
import logging
import socketserver
import threading
import time
import uuid

import base
import console
import db
import exceptions as exc
import package

logging.basicConfig(format="%(asctime)s.%(msecs)03d\t%(message)s", datefmt="%H:%M:%S",
                    level=logging.INFO, filename="../log.txt")


class ThreadingRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        request = self.get_request()

        try:
            response = self.authorization(request)
            if not response:
                response = self.handle_request(request)
        except exc.BaseError as e:
            response = self.handle_error(e, 400)

        return self.do_response(response)

    def handle_request(self, request):
        execute = request.headers.get("execute")
        if execute:
            if execute.lower() == "/shutdown":
                self.server.shutdown(10)
                request.content = "The server will be shutdown in 10 seconds."
                return request

        request.content = f"Greeting from server:\n'hello, {request.headers.get('username')}'"
        return request

    def handle_error(self, e, status=400):
        status = e.status or status
        return package.Package(status=status, content=e.message)

    def get_request(self):
        raw_request = self.rfile.read(1024)
        while True:
            data = self.rfile.read(1024)
            if not data:
                break

            raw_request += data

        request = package.Package.from_bytes(raw_request)
        logging.info(f"Thread: {threading.current_thread().name}")
        logging.info(f"Received from {':'.join(map(str, self.client_address))}:\n {request}\n")
        return request

    def do_response(self, response: package.Package):
        logging.info(f"Sent to {':'.join(map(str, self.client_address))}:\n {response}\n")
        return self.wfile.write(response.to_bytes())

    def authorization(self, request):
        try:
            not_authorized = not self.is_authorized(request.headers, request.cookies)
        except exc.AuthorizationError as e:
            return self.handle_error(e)

        if not_authorized:
            try:
                return self.do_log_in(request.headers, request.cookies)
            except exc.AuthorizationError as e:
                return self.handle_error(e)

    def do_log_in(self, headers, cookies):
        username = headers.get("username")
        password = headers.get("password")

        if username is None or password is None:
            raise exc.AuthorizationError(message="The user is not logged in. "
                                                 "Headers with parameters are required: "
                                                 "'username', 'password'",
                                         status=403)

        current_user = db.DataBase.session.query(db.User).filter_by(username=username).one_or_none()
        if current_user is None:
            raise exc.UserNotExistError

        if hashlib.md5(password.encode()).hexdigest() != current_user.password:
            raise exc.PasswordError

        session_token = str(uuid.uuid4())
        current_user.session_token = session_token

        session_start = datetime.datetime.now()
        current_user.session_start = session_start

        with db.DataBase.session.begin() as transaction:
            try:
                db.DataBase.session.add(current_user)
            except Exception as e:
                logging.info(f"Error: {e}")
                transaction.rollback()

        return package.Package(status=200,
                               content=f"Authorization is successful!\nWelcome, {username}",
                               headers={
                                   **headers
                               },
                               cookies={
                                   **cookies,
                                   "session-token": session_token,
                                   "session-start": session_start.strftime("%H:%M:%S - %m.%d.%Y")
                               })

    def is_authorized(self, headers, cookies):
        session_timeout = 15 * 60

        username = headers.get("username")
        if username is None:
            raise exc.UsernameIsNoneError

        current_user = db.DataBase.session.query(db.User).filter_by(username=username).one_or_none()
        if current_user is None:
            raise exc.UserNotExistError(username=username)

        session_token = current_user.session_token
        if session_token is None:
            return False

        session_start = current_user.session_start
        if session_start is None:
            return False

        if datetime.datetime.now() - session_start > datetime.timedelta(seconds=session_timeout):
            return False

        if session_token != cookies.get("session-token"):
            return False

        return True


class ThreadingServer(base.ThreadingTCPServer):
    daemon_threads = True

    def __init__(self, server_address, request_handler, console_handler=None, bind_and_activate=True):
        super(ThreadingServer, self).__init__(server_address, request_handler, bind_and_activate)
        self.console_handler = console_handler(self)

    def server_bind(self):
        self.socket.setblocking(False)
        super(ThreadingServer, self).server_bind()

        host, port = self.server_address
        logging.info(f"Server was bound:\t{host}:{port}")

    def server_activate(self):
        super(ThreadingServer, self).server_activate()
        logging.info("Server started listening")

    def serve_forever(self, poll_interval=0.5):
        try:
            super(ThreadingServer, self).serve_forever(poll_interval)
        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self, timeout=3):
        threading.Thread(target=self._shutdown, args=[timeout]).start()

    def _shutdown(self, timeout):
        for i in range(timeout, 0, -1):
            logging.info(f"Server shutdown in {i} sec...")
            time.sleep(1)

        super(ThreadingServer, self).shutdown()

    def get_request(self):
        request, client_address = super(ThreadingServer, self).get_request()
        host, port = client_address
        logging.info(f"New connection from:\t{host}:{port}")
        return request, client_address

    def close_request(self, request):
        host, port = request.getpeername()
        logging.info(f"Close connection:\t{host}:{port}")
        super(ThreadingServer, self).close_request(request)

    def server_close(self):
        super(ThreadingServer, self).server_close()
        logging.info(f"Server is shutdown!")


if __name__ == "__main__":
    HOST, PORT = "localhost", 40096

    with ThreadingServer((HOST, PORT), ThreadingRequestHandler, console.Console) as server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        server.console_handler.serve_forever()

        server.shutdown()
