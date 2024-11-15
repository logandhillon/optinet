from typing import List

from optinet.layer.presentation import Sequencer
from optinet.layer.transport import GTPPacket
from optinet.networking import IPacket
from optinet.lib import CTRL


class OCP:
    def prepare(packet: IPacket, src: bytes, dest: bytes):
        return Sequencer.to_spectral(CTRL.SOH.value+src+dest+CTRL.STX.value) + packet.data + Sequencer.to_spectral(CTRL.ETX.value)

    @staticmethod
    def send(packets: List[IPacket]):
        for packet in packets:
            packet = OCP.prepare(packet, b'0000', b'0000')
            for code in packet:
                print(code)


if __name__ == "__main__":
    OCP.send(
        GTPPacket.create_packets(
            Sequencer.to_spectral(b"Hello world! this is a long payload... how many packets?")))
