from binascii import unhexlify
from pwn import xor

solvethis = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

key = solvethis[0] ^ ord('c')
print(''.join(chr(c ^ key) for c in solvethis))