
def encode(text):
    binary_text = ''
    for symb in text:
        bin_symb = str(bin(ord(symb))).replace("0b", '')
        binary_text += (8 - len(bin_symb)) * '0' + bin_symb
    return binary_text


def crack(text):
    words = ''
    for i in range(0, len(text) - 1, 8):
        byte = int(text[i: i + 8], 2)
        words += chr(byte)
    return words
