from __future__ import (absolute_import, division, print_function, unicode_literals)
import base64

def encode_base64(data):
    encoded = base64.b64encode(data.encode())
    print("\n---> Encoded message is: " + encoded.decode())

    return encoded

def decode_base64(data):
    decoded = base64.b64decode(data).decode()
    print("\n---> Decoded message is: " + str(decoded))

    return decoded

filepath = 'raw_text.txt'
with open(filepath) as file:
    contents = file.read()

encoded_contents = encode_base64(contents)
decoded_again_contents = decode_base64(encoded_contents)