from binascii import unhexlify
from pwn import xor


key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1and2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2and3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


key2 = xor(bytes.fromhex(key1and2), key1)
key3 = xor(bytes.fromhex(key2and3), key2)
flag_key123 = xor(bytes.fromhex(key1and2), key3)

flag = xor(bytes.fromhex(flag_key), flag_key123)

print("The flag is:", flag.decode())