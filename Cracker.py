import Code
import time
import re
import Dictionary
import Colors


def cracker(string, mode, beautiful_print=1): # 0 - Default and hash cracking 1 - Bruteforce cracking
    encryption = Encryption(string)

    if mode == 0:
        possible_groups = ['default', 'hash']

    elif mode == 1:
        possible_groups = ['bruteforce']

    if beautiful_print:
        print(Colors.default_color + '\nCalculating possible algorithms...')

    possible_algorithms = encryption.getPossible(possible_groups)

    if beautiful_print:
        print(Colors.default_color + '\n> Possible Ciphers:\n', Colors.decode_color +
              str(possible_algorithms))
    
    cracking = Cracking(possible_algorithms, string)

    if beautiful_print:
        print(Colors.default_color + '\nDecoding...')

    return cracking.crack()


class Encryption():

    def __init__(self, string: str):
        self.dictionary = Dictionary.get()

        self.string = string
        self.string_length = len(self.string)


    def getPossible(self, groups=[]):
        possible_ciphers = []

        for cipher_name, cipher in self.dictionary.items():
            if cipher['group'] not in groups and len(groups) != 0:
                continue
            
            if self.checkCipher(cipher_name):
                possible_ciphers.append(cipher_name)

        return possible_ciphers


    def checkCipher(self, cipher_name: str):
        cipher = self.dictionary[cipher_name]
        
        cipher_length = cipher['length']
        regular_string = cipher['regular_string']

        is_true_lenght = self.check_length(cipher_length)

        is_string_true = self.check_regular(regular_string, self.string)

        return is_true_lenght and is_string_true


    def check_length(self, cipher_length):
        if cipher_length == -1:
            return 1

        return cipher_length == self.string_length


    def check_regular(self, regular_string, string):
        result = re.match(regular_string, string)

        return (not result is None) and result.group(0) == string 
    

class Cracking():

    def __init__(self, ciphers: list, string: str):
        self.dictionary = Dictionary.get()
        self.ciphers = ciphers
        self.string = string


    def crack(self):
        answer = dict()

        for cipher in self.ciphers:
            answer[cipher] = self.tryToCrack(cipher)

        return answer

    def tryToCrack(self, cipher):
        answer = {"error": 0, "result": 0, "group": self.dictionary[cipher]["group"]}

        try:
            result = Code.Crack(self.string, cipher)
        except Exception as ex:
            result = str(ex)
            answer["error"] = 1

        answer["result"] = result
        
        return answer
