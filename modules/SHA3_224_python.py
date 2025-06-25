from modules import hasher


def crack(HASH):
    type_of_hash = 'SHA3-224'
    num_of_hash = 17300
    return hasher.getFraze(type_of_hash, HASH, num_of_hash)
