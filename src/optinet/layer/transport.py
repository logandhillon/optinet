from typing import List, Tuple

from optinet.layer.presentation import Sequencer
from optinet.networking import IPacket


class GTPPacket(IPacket):
    MAX_PACKET_SIZE = 16    # how many hex codes in a packet

    def __init__(self, data: List[str]) -> None:
        if (len(data) > GTPPacket.MAX_PACKET_SIZE):
            raise ValueError("packet too large!")
        super().__init__(data, "GTP")

    @staticmethod
    def send(self):
        for code in self.data:
            print(code)
        input("Press RETURN to simulate ACK...")

    @staticmethod
    def create_packets(spectral_payload: List[Tuple[str]]):
        chunks = [spectral_payload[i:i + GTPPacket.MAX_PACKET_SIZE] for i in range(0, len(spectral_payload), GTPPacket.MAX_PACKET_SIZE)]
        return [GTPPacket(chunk) for chunk in chunks]


class GTP:
    @staticmethod
    def send(packets: List[GTPPacket]):
        for packet in packets:
            packet.send()


if __name__ == "__main__":
    GTP.send(GTPPacket.create_packets(Sequencer.to_spectral(b"Hello world! this is a long payload... how many packets?")))
    print(GTPPacket(["asd", "fgh"]))
