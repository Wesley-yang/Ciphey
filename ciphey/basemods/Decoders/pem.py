from typing import Optional, Dict

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import cryptography.exceptions

from ciphey.iface import Decoder, Der, Config, X509, ParamSpec


class PemDer(Decoder[str, Der]):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "pem"

    def decode(self, ctext: str) -> Optional[Der]:
        try:
            return load_pem_private_key(ctext, None, backend=default_backend())
        except ValueError:
            pass
        except cryptography.exceptions.UnsupportedAlgorithm:
            pass

    @staticmethod
    def priority() -> float:
        return 0.01

    def __init__(self, config: Config):
        super().__init__(config)


class PemX509(Decoder[str, X509]):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "pem"

    def decode(self, ctext: str) -> Optional[Der]:
        try:
            return load_pem_private_key(ctext, None, backend=default_backend())
        except ValueError:
            pass
        except cryptography.exceptions.UnsupportedAlgorithm:
            pass

    @staticmethod
    def priority() -> float:
        return 0.01

    def __init__(self, config: Config):
        super().__init__(config)