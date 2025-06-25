def encode(string):
    encoded_string = ''

    for symb in string:
        encoded_string += str(ord(symb)) + ' '

    return encoded_string[:-1]


def crack(encoded_string):
    string = ''

    for byte in encoded_string.strip().split():
        string += chr(int(byte))

    return string
