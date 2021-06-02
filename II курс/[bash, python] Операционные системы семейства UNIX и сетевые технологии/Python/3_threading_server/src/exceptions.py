class BaseError(Exception):

    def __init__(self, message="", status=None):
        self.message = message
        self.status = status


class AuthorizationError(BaseError):

    def __init__(self, message="", username=None, password=None, status=400):
        super(AuthorizationError, self).__init__(message, status)
        self.username = username
        self.password = password


class UserNotExistError(AuthorizationError):
    message = "User with username '{username}' not found!"

    def __init__(self, username):
        super(UserNotExistError, self).__init__(message=self.message, username=username)
        self.message = self.message.format(username=username)


class UsernameIsNoneError(AuthorizationError):
    message = "Header 'username' is required"

    def __init__(self):
        super(UsernameIsNoneError, self).__init__(message=self.message)


class PasswordError(AuthorizationError):
    message = "Invalid username-password pair"

    def __init__(self):
        super(PasswordError, self).__init__(message=self.message)
