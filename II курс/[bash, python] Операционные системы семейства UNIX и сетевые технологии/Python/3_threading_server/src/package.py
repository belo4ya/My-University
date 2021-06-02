import json
import pprint
import struct


class Package:
    ENCODING = "utf-8"
    STATUS_LEN = 2
    HEADER_LEN = 2

    def __init__(self, headers=None, cookies=None, content="", status=200):
        self.status = status
        self.headers = headers or {}
        self.cookies = cookies or {}
        self.content = content

    @classmethod
    def from_bytes(cls, data: bytes) -> "Package":
        status = cls._decode_fixed_length_header(data[:cls.STATUS_LEN])
        data = data[cls.STATUS_LEN:]

        headers_len = cls._decode_fixed_length_header(data[:cls.HEADER_LEN])
        data = data[cls.HEADER_LEN:]

        headers = cls.json_decode(data[:headers_len])
        data = data[headers_len:]

        cookies_len = headers.get("cookies-length") or 0
        cookies = cls.json_decode(data[:cookies_len])
        data = data[cookies_len:]

        content_len = headers.get("content-length") or 0
        content = cls.json_decode(data[:content_len])

        return Package(headers, cookies, content, status)

    def to_bytes(self) -> bytes:
        encoding = self.headers.get("encoding") or self.ENCODING

        content = self.json_encode(self.content, encoding)
        cookies = self.json_encode(self.cookies, encoding)

        self.headers["content-length"] = len(content)
        self.headers["cookies-length"] = len(cookies)
        headers = self.json_encode(self.headers, encoding)

        status = self._encode_fixed_length_header(self.status)
        headers_len = self._encode_fixed_length_header(len(headers))

        return status + headers_len + headers + cookies + content

    @staticmethod
    def _encode_fixed_length_header(data) -> bytes:
        return struct.pack(">H", data)

    @staticmethod
    def _decode_fixed_length_header(bytes_obj):
        return struct.unpack(">H", bytes_obj)[0]

    @staticmethod
    def json_encode(data, encoding) -> bytes:
        return json.dumps(data).encode(encoding)

    @staticmethod
    def json_decode(json_obj):
        return json.loads(json_obj)

    def __str__(self):
        return pprint.pformat({
            "status": self.status,
            "headers": self.headers,
            "cookies": self.cookies,
            "content": self.content
        }, sort_dicts=False)

    __repr__ = __str__
