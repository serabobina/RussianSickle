from modules import hasher


def crack(HASH):
    type_of_hash = 'SHA-1'
    num_of_hash = 100
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
