from typing import List, Tuple

FACTOR_5_TO_8 = 255/31
FACTOR_6_TO_8 = 255/63


class Sequencer:
    @staticmethod
    def bytes_to_565s(data: bytes):
        if len(data) % 2 != 0:
            data += b'\x00'

        seqs = []
        for i in range(0, len(data), 2):
            seq = f"{data[i]:08b}{data[i + 1]:08b}"
            seqs.append((int(seq[:5], 2), int(seq[5:11], 2), int(seq[11:16], 2)))

        return seqs

    @staticmethod
    def _565s_to_bytes(seqs: List[Tuple[int]]):
        out = bytearray()

        for seq in seqs:
            b1 = f"{seq[0]:05b}{seq[1]:06b}"[:-3]
            b2 = f"{seq[1]:06b}{seq[2]:05b}"[3:]
            # out.append((int(b1, 2), int(b2, 2)))
            out.append(int(b1, 2))
            out.append(int(b2, 2))

        return bytes(out)

    @staticmethod
    def to_spectral(data: bytes):
        seqs = Sequencer.bytes_to_565s(data)
        out = []

        for seq in seqs:
            out.append(f"{round(seq[0] * FACTOR_5_TO_8):02x}{round(seq[1] * FACTOR_6_TO_8):02x}{round(seq[2] * FACTOR_5_TO_8):02x}")

        return out

    @staticmethod
    def from_spectral(data: List[str]):
        seq = []

        for code in data:
            seq.append((
                round(int(code[:2], 16)/FACTOR_5_TO_8),
                round(int(code[2:4], 16)/FACTOR_6_TO_8),
                round(int(code[4:6], 16)/FACTOR_5_TO_8)))

        return Sequencer._565s_to_bytes(seq)


if __name__ == "__main__":
    text = input("Enter plaintext: ").encode()
    print(len(text), "bytes")
    print("Encoded:", Sequencer.to_spectral(text))
    decoded = Sequencer.from_spectral(Sequencer.to_spectral(text))
    print(f"Decoded: '{decoded.decode()}' ({len(decoded)} bytes) (RAW: {decoded})")
