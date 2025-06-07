
def encode(text):
    binary_text = ''
    for symb in text:
        bin_symb = str(bin(ord(symb)))
        binary_text += bin_symb.replace("0b", '') + ' '
    return binary_text[:-1]


def crack(text):

    words = ''
    for word in text.split():
        words += chr(int(word, 2))
    return words




