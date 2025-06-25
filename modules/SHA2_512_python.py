from modules import hasher


def crack(HASH):
    type_of_hash = 'SHA2-512'
    num_of_hash = 1700
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
