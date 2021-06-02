import logging
import db


class Console:

    def __init__(self, server):
        self.log_file = logging.getLogger().handlers[0].baseFilename
        self.server = server
        self._finish_request = self.server.finish_request

    def serve_forever(self):
        commands = {
            "/shutdown": self.server.shutdown,
            "/stop": self.stop,
            "/start": self.start,
            "/logs": self.logs,
            "/clear-logs": self.clear_logs,
            "/clear-users": self.clear_users
        }
        while True:
            execute = str(input(">>> ")).lower()
            cmd = commands.get(execute)
            if cmd is not None:
                cmd()
            else:
                print(f"Unidentified command: {execute}")

    def stop(self):
        def plug(request, client_address):
            return

        self._finish_request = self.server.finish_request
        self.server.finish_request = plug

    def start(self):
        self.server.finish_request = self._finish_request

    def logs(self):
        with open(self.log_file, mode="r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())

    def clear_logs(self):
        with open(self.log_file, mode="w", encoding="utf-8"):
            pass

    def clear_users(self):
        with db.DataBase.session.begin() as transaction:
            try:
                users = db.DataBase.session.query(db.User).all()
                for user in users:
                    user.session_token = None
                db.DataBase.session.add_all(users)
            except Exception as e:
                transaction.rollback()
