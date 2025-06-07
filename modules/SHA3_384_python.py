from modules import hasher

def crack(HASH):
    type_of_hash = 'SHA3-384'
    num_of_hash = 17500
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
