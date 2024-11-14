[❮ Back](index.md)

# Optinet OSI model

## Physical Layer (L1)

Input: camera or other light sensor.

Output: screen or other light emmitter.

Protocols that use the spectral sequencer must support colour on I/O layer 1.

## Data Link Layer (L2)

## Spectral sequencer (5-6-5)

Transforms the bytes into a color sequence using 5-6-5 RGB encoding.

Only 2 bytes can be stored in one color.

- 5-bit = DEC 0-31 ($2^5$)
  - To 8-bit: $x\times\frac{255}{31}$
- 6-bit = DEC 0-63 ($2^6$)
  - To 8-bit: $x\times\frac{255}{63}$
- 8-bit = DEC 0-255 ($2^8$)
  - To 5-bit: $x\div\frac{255}{31}$
  - To 6-bit: $x\div\frac{255}{63}$

**Example:** `"AB"` (ASCII 65, 66 &rarr; 0b01000001, 0b01000010 &rarr; 0100000101000010):

- Scale 8-bit into 5-6-5
  - Red (first 5 bits): 01000 (8) &rarr; to 8-bit &rarr; $8\times\frac{255}{31} = 65.80... \approx 66$ (0x42)
  - Green (next 6 bits): 001010 (10) &rarr; to 8-bit &rarr; $10\times\frac{255}{63} = 40.48... \approx 40$ (0x28)
  - Blue (last 5 bits): 00010 (2) &rarr; to 8-bit &rarr; $2\times\frac{255}{31} = 16.45... \approx 16$ (0x10)
- Combine into a color: `#422810`

∴ `"AB"` = `#422810`

**Example:** `#422810` &rarr; `rgb(66, 40, 16)`:

- Scale 5-6-5 into 8-bit
  - Red (first 5 bits): 66 &rarr; to 5-bit &rarr; $66\div\frac{255}{31} = 8.02... \approx 8$ (0b1000 =(pad leading zeros)=> 01000)
  - Green (next 6 bits): 40 &rarr; to 6-bit &rarr; $40\div\frac{255}{63} = 9.88... \approx 10$ (0b1010 =(pad leading zeros)=> 001010)
  - Blue (last 5 bits): 16 &rarr; to 5-bit &rarr; $16\div\frac{255}{31} = 1.95... \approx 2$ (0b10 =(pad leading zeros)=> 00010)
- Reshape sequence from 5-6-5 to 8-bit (01000, 001010, 00010 &rarr; 0100000101000010 &rarr; 01000001, 01000010)
- Convert BIN to DEC (01000001, 01000010 &rarr; 65, 66)

∴ `#422810` = `65, 66` &rarr; `ASCII A, B` &rarr; `"AB"`

## Binary sequencer

Transforms the bytes into a binary sequence

**Example:** `"AB"` (ASCII 65, 66 &rarr; 0b01000001, 0b01000010 &rarr; 0100000101000010)

## Network Layer (L3)

Handles routing and forwarding of data between networks.
Protocols: IP (Internet Protocol), ICMP (for error reporting like ping), OSPF.

## Transport Layer (L4)

Ensures reliable data transfer between systems.
Protocols: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).

## Session Layer (L5)

Manages sessions between applications.
Rarely used as a distinct layer in modern networking.

## Presentation Layer (L6)

Handles data formatting, encryption, and compression.
Protocols: SSL/TLS for encryption, which is used by HTTPS.

## Application Layer (L7)

Provides services for user-facing applications.
Protocols: HTTP, HTTPS, FTP, SMTP, DNS.

OP address
its a colour yeah thats it fire ???
