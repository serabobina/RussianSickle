import json
import os
import config


base_path = config.DIR_PATH + 'dictionary/dictionary.json'

def get():
    with open(base_path) as file:
        return json.load(file)
        
def add(new: tuple):
    old = get()
    old[new[0]] = new[1]
        
    create(old)

def create(default):
    with open(base_path, 'w') as file:
        json.dump(default, file)
            
    return len(str(default))

def delete(cipher):
    old = get()
    if cipher in old:
        del old[cipher]
    create(old)