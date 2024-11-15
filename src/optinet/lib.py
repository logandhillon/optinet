from enum import Enum


class CTRL(Enum):
    SOH = b'\x01'
    STX = b'\x02'
    ETX = b'\x03'
    EOT = b'\x04'
    ACK = b'\x06'
