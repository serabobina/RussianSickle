import config
from modules import base64_python
from modules import morse_python
from modules import hexedimical_python
from modules import binary_python
from modules import binary2_python
from modules import caesar_python
from modules import ASCII_python
from modules import rail_fence_python
from modules import URI_python
from modules import scytale_python
from modules import MD5_python
from modules import SHA_1_python
from modules import SHA2_224_python
from modules import SHA2_256_python
from modules import SHA2_384_python
from modules import SHA2_512_python
from modules import SHA3_224_python
from modules import SHA3_256_python
from modules import SHA3_384_python
from modules import SHA3_512_python


functions = {'Base64': base64_python, 'Morse': morse_python,
             'Hexedimical': hexedimical_python, 'Binary': binary_python,
             'Binary2': binary2_python, 'Caesar': caesar_python,
             'ASCII': ASCII_python, 'Rail Fence': rail_fence_python,
             'URL encoding': URI_python, 'Scytale': scytale_python,
             'MD5': MD5_python, 'SHA-1': SHA_1_python,
             'SHA2-224': SHA2_224_python, 'SHA2-256': SHA2_256_python,
             'SHA2-384': SHA2_384_python, 'SHA2-512': SHA2_512_python,
             'SHA3-224': SHA3_224_python, 'SHA3-256': SHA3_256_python,
             'SHA3-384': SHA3_384_python, 'SHA3-512': SHA3_512_python}


def Crack(string, cipher):
    decoded_string = functions[cipher].crack(string)
    
    return decoded_string


def Encode(string, cipher):
    encoded_string = functions[cipher].encode(string)
    
    return encoded_string
    
