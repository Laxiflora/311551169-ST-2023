import struct
byt = b'194223069723458251202546309576351126056411599334913961246881117330281138570713811115087539186563221222181426122318026510126242397028715542292552253009'
byte_stream = b'\x91za\x7f\xe4DvU\xb0@}\x90\x8c\xb8\x97S\xeb\xb5\x9d\x1d\xd7BQP5\xc4\x1c\xea\xa3\x03v\xf2\xbbv\x81t\xca\xec\xf1\xd60H\xf0\x9a\x80=\x9b\xc6\x8c\xf2z\xe2\xbbH\xefl\xbf*\xf6\xbf'

a = byte_stream[:2]
print(a)
a = int.from_bytes(a, byteorder='little')
print(f"a = {a}")


b_stream = b''
b = byte_stream[:4]
b = int.from_bytes(b, "big")
print(f"b = {b}")

c = byte_stream[:0x20]
c = c.decode()
print(c)

#----
integer_list = struct.unpack('i' * (len(byte_stream)//4), byte_stream)
print(integer_list)