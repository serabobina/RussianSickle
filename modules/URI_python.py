import urllib.parse

def encode(string):
    return urllib.parse.quote(string)

def crack(string): 
    return urllib.parse.unquote(string)

