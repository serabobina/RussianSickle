from modules import hasher

def crack(HASH):
    type_of_hash = 'MD5'
    num_of_hash = 0
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
