# Реализация шифра Вернама


class OneTimePad:
    """
    >>> message = 'KOD'
    >>> cypher = OneTimePad('­z«')
    >>> cypher.encrypt(message)
    'æ5ï'
    >>> cypher.decrypt('æ5ï')
    'KOD'
    """

    def __init__(self, key: str):
        self._key = key

    def encrypt(self, message: str) -> str:
        assert len(message) == len(self._key)

        return ''.join([chr(ord(c) ^ ord(self._key[i])) for i, c in enumerate(message)])

    def decrypt(self, encrypted: str) -> str:
        assert len(encrypted) == len(self._key)

        return ''.join([chr(self._rxor(ord(c), ord(self._key[i]))) for i, c in enumerate(encrypted)])

    def _rxor(self, a: int, b: int) -> int:
        bin_a = format(a, '#010b')
        bin_b = format(b, '#010b')

        rxor = ''
        for i, c in enumerate(bin_b):
            if c == '1':
                rxor += '0' if bin_a[i] == '1' else '1'
            else:
                rxor += bin_a[i]

        return int(rxor, 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
