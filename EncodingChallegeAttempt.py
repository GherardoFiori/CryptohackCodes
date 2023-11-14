from pwn import * # pip install pwntools
import json
import base64
import binascii 
import codecs
import sys

def decoding(a, value):
    if a == 'base64':
        return base64.b64decode(value).decoded('utf-8')
    elif a == 'hex':
        return binascii.unhexlify(value).decoded('utf-8')
    elif a == 'biginit':
        return binascii.unhexlify(value).decoded('utf-8')
    elif a == 'rot13':
        return codecs.encode(value, 'rot_13')
    elif t == 'utf-8':
        b = ""
        for c in value:
            b += chr(c)
        return b

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

to_send = {
    "decoded": "changeme"
}
json_send(to_send)
json_recv()
