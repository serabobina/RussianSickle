from modules import hasher

def crack(HASH):
    type_of_hash = 'SHA3-256'
    num_of_hash = 14400
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
