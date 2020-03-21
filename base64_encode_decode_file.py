from __future__ import (absolute_import, division, print_function, unicode_literals)
import json
import base64

filepath = 'encoded.json'
# filepath = 'raw_text.json'
with open(filepath, 'rb') as file:
    contents = json.load(file)

for items in contents:
    encoded = int(items['encode'])
    title = items['title']
    content = items['content']
    # print("encode is {}, title type is {}, content type is {}".format(encoded, type(title), type(content)))

def encode_base64(data):
    encoded = base64.b64encode(data.encode())
    print("\n---> Encoded message is: " + encoded.decode())

    return encoded

def decode_base64(data):
    decoded = base64.b64decode(data.encode()).decode()
    print("\n---> Decoded message is: " + str(decoded))

    return decoded

if encoded == 0:
    print("\nOriginal Title: " + title, end='')
    encode_base64(title)
    print("\nOriginal Content: " + content, end='')
    encode_base64(content)
elif encoded == 1:
    print("\nEncoded Title: " + title, end='')
    decode_base64(title)
    print("\nEncoded Content: " + content, end='')
    decode_base64(content)
else:
    print("\nThe format of your json file should be encode: ,title: ,content:, ***")