from typing import List, Self, Tuple


class IPacket:
    def __init__(self, data: List[str], protocol: str = "") -> None:
        if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
            raise TypeError("data must be a list of colour hex codes")
        self.data = data
        self.protocol = protocol

    @staticmethod
    def create_packets(spectral_payload: List[Tuple[str]]) -> List[Self]:
        raise NotImplementedError("create_packets must be implemented")

    def __repr__(self) -> str:
        return f"<{self.protocol}Packet with {len(self.data)} frames>"
