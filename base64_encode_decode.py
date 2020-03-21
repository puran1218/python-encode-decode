import base64

def encode_base64(data):
    encoded = base64.b64encode(data.encode())
    print("\n---> Encoded message is: " + encoded.decode())

    return encoded

def decode_base64(data):
    decoded = base64.b64decode(data.encode()).decode()
    print("\n---> Decoded message is: " + str(decoded))

    return decoded

prompt = "\nDo you want to encode or decode message? Or you can enter 'quit' to end the program. 'encode'/'decode'/'quit': "

active = True
while active:
    message = input(prompt)

    if message == 'encode':
        encode_message = input("\nPlease input the message you want to encode: ")
        encode_base64(encode_message)
    elif message == 'decode':
        decode_message = input("\nPlease input the message you want to decode: ")
        decode_base64(decode_message)
    elif message == 'quit':
        active = False
    else:
        print("\n*** Please input 'encode', 'decode', or 'quit'. ***")