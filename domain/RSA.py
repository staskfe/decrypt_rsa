from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import date

key = b''


class RSA:
    _instance = None
    _last_instance = None

    def __init__(self):
        self.private_key = load_pem_private_key(key, None)

    @classmethod
    def instance(cls):
        if cls._instance is None or cls._last_instance > date.today():
            cls._instance = cls()
            cls._last_instance = date.today()
        return cls._instance

    def get_public_key(self):
        public_key = self.private_key.public_key()

        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def decrypt(self, message):
        return self.private_key.decrypt(message, padding.PKCS1v15())
