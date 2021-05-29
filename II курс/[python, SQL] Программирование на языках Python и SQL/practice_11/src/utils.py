import re


def task(n):
    def wrapper(function):
        def decorator(*args, **kwargs):
            print(str(n) + ". " + re.sub(r' +', ' ', function.__doc__.strip()) + "\n")
            result = function(*args, **kwargs)
            print('\n\n')
            return result
        return decorator
    return wrapper
