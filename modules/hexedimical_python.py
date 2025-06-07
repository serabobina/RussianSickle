
def crack(hex_text):

    text = ''
    hex_numbers = hex_text.strip().split()
    for hex_number in hex_numbers:
        number = int(hex_number, 16)
        text += chr(number)
    return text


def encode(text):
    hex_text = ''
    for symb in text:
        hex_symb = hex(ord(symb)).replace("0x", '')
        hex_text += hex_symb
        hex_text += ' '
    hex_text = hex_text[:-1]
    return hex_text


