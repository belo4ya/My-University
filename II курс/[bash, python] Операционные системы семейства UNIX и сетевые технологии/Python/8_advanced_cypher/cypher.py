class DiffieHellman:
    """Набор методов для реализации протокола Диффи-Хеллмана"""

    def __init__(self, g: int, p: int, secret: int):
        self._g = g
        self._p = p
        self._secret = secret

    def compute_public(self) -> int:
        return self._g ** self._secret % self._p

    def compute_key(self, public: int) -> int:
        return public ** self._secret % self._p


class Caesar:
    """Упрощенная версия шифра цезаря (без возможности задать алфавит)"""

    @staticmethod
    def encrypt(message: str, key: int) -> str:
        return Caesar._apply_shift(message, key)

    @staticmethod
    def decrypt(encrypted: str, key: int) -> str:
        return Caesar._apply_shift(encrypted, -key)

    @staticmethod
    def _apply_shift(string: str, shift: int) -> str:
        max_digit = int('0x110000', 16)  # номер последнего символа функции chr()
        return ''.join([chr((ord(c) + shift) % max_digit) for c in string])
