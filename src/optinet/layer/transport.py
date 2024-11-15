from typing import List, Tuple

from optinet.layer.presentation import Sequencer


class GTPPacket:
    MAX_PACKET_SIZE = 16    # how many hex codes in a packet

    def __init__(self, data: List[str]) -> None:
        if (len(data) > GTPPacket.MAX_PACKET_SIZE):
            raise ValueError("packet too large!")
        if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
            raise TypeError("data must be a list of colour hex codes")

        self.data = data

    @staticmethod
    def create_packets(spectral_payload: List[Tuple[str]]):
        chunks = [spectral_payload[i:i + GTPPacket.MAX_PACKET_SIZE] for i in range(0, len(spectral_payload), GTPPacket.MAX_PACKET_SIZE)]
        return [GTPPacket(chunk) for chunk in chunks]

    def __repr__(self) -> str:
        return f"<GTPPacket with {len(self.data)} frames>"


class GTPIO:
    @staticmethod
    def send(packets: List[GTPPacket]):
        for packet in packets:
            for code in packet.data:
                print(code)
            input("Press RETURN to simulate ACK...")


if __name__ == "__main__":
    GTPIO.send(GTPPacket.create_packets(Sequencer.to_spectral(b"Hello world! this is a long payload... how many packets?")))
