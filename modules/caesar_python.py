import random
from modules import brute_force

eng_alth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ru_alth = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
           'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

eng_alth_up = list(map(str.upper, eng_alth))
ru_alth_up = list(map(str.upper, ru_alth))


def Caesar(string, offset):
    encoded_string = ''

    for symb in string:
        if symb.isalpha():
            alth = getAlth(symb)
            start = alth[0]
            length = len(alth)

            symb = alth[(alth.index(symb) + offset) % length]

        encoded_string += symb

    return encoded_string


def Decode(string, key):
    return Caesar(string, -key)


def getAlth(symb):
    if symb in eng_alth:
        return eng_alth
    if symb in ru_alth:
        return ru_alth
    if symb in eng_alth_up:
        return eng_alth_up
    if symb in ru_alth_up:
        return ru_alth_up


def getRange(string):
    start = 1
    max_end = 26

    for symb in string:
        if symb.isalpha():
            end = len(getAlth(symb))
            if end > max_end:
                max_end = end

    return (start, max_end)


def encode(string):
    offset = random.randint(1, len(string) - 1)

    return Caesar(string, offset)


def crack(string):
    brute_range = getRange(string)
    return brute_force.bruteForce(string, brute_range, Decode)
