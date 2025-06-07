import random
from modules import brute_force

def Encode(string, key, return_array=0):
    rays = [[] for _ in range(key)]
    encoded_string = []
        
    count = 0
    tend = 1
    for symb in string:
        rays[count].append(symb)
        if count == 0:
            tend = 1
        elif count == key - 1:
            tend = -1
            
        count += tend

    for ray in rays:
        for symb in ray:
            encoded_string.append(symb)


    if not return_array:
        encoded_string = ''.join(encoded_string)

        
    return encoded_string

def encode(string):
    key = random.randint(1, len(string))

    return Encode(string, key)

def crack(string):
    brute_range = (2, len(string) + 1)
    return brute_force.bruteForce(string, brute_range, Decode)
    
def Decode(string, key):
    decode_table = []
    for i in range(0, len(string)):
        decode_table.append(str(i))

    encoded_table = Encode(decode_table, key, return_array=1)
    
    decoded_list = [''] * len(string)

    
    for i in range(len(encoded_table)):
        decoded_list[decode_table.index(encoded_table[i])] = string[i]

    decoded_string = ''
    for i in range(len(decoded_list)):
        decoded_string += decoded_list[i]

    return decoded_string



    
