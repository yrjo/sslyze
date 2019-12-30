from enum import Enum
from typing import Dict, Type, TYPE_CHECKING

from sslyze.plugins.certificate_info.scan_commands import CertificateInfoImplementation
from sslyze.plugins.openssl_cipher_suites.scan_commands import Sslv20ScanImplementation, Sslv30ScanImplementation, \
    Tlsv10ScanImplementation, Tlsv13ScanImplementation, Tlsv12ScanImplementation, Tlsv11ScanImplementation

if TYPE_CHECKING:
    from sslyze.plugins.plugin_base import ScanCommandImplementation


class ScanCommandEnum(Enum):
    CERTIFICATE_INFO = "certinfo"

    SSL_2_0_CIPHER_SUITES = "sslv2"
    SSL_3_0_CIPHER_SUITES = "sslv3"
    TLS_1_0_CIPHER_SUITES = "tlsv1_0"
    TLS_1_1_CIPHER_SUITES = "tlsv1_1"
    TLS_1_2_CIPHER_SUITES = "tlsv1_2"
    TLS_1_3_CIPHER_SUITES = "tlsv1_3"

    def _get_implementation_cls(self):
        return _IMPLEMENTATION_CLASSES[self]


# TODO(AD): Test this
_IMPLEMENTATION_CLASSES: Dict[ScanCommandEnum, Type["ScanCommandImplementation"]] = {
    ScanCommandEnum.CERTIFICATE_INFO: CertificateInfoImplementation,
    ScanCommandEnum.SSL_2_0_CIPHER_SUITES: Sslv20ScanImplementation,
    ScanCommandEnum.SSL_3_0_CIPHER_SUITES: Sslv30ScanImplementation,
    ScanCommandEnum.TLS_1_0_CIPHER_SUITES: Tlsv10ScanImplementation,
    ScanCommandEnum.TLS_1_1_CIPHER_SUITES: Tlsv11ScanImplementation,
    ScanCommandEnum.TLS_1_2_CIPHER_SUITES: Tlsv12ScanImplementation,
    ScanCommandEnum.TLS_1_3_CIPHER_SUITES: Tlsv13ScanImplementation,
}