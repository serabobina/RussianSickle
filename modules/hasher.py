import Colors

fraze = f"""{Colors.default_color}It looks like this string is an %TYPE_OF_HASH hash. It is impossible to decrypt it, but you can pick it up using a dictionary. To do this, you need to install {Colors.greed_color}Hashcat{Colors.default_color}. The official website is {Colors.greed_color}https://hashcat.net/hashcat/{Colors.default_color}. Also, to pick up using a dictionary, you need to download a dictionary. Examples of dictionaries are {Colors.greed_color}https://github.com/ileygb8cwqogn8c/different_lists{Colors.default_color}. If you already have this utility installed on your system and you have a dictionary, follow these steps to pick up this string using a dictionary:

Linux:
1) {Colors.greed_color}%HASH > your_hash.hash
{Colors.default_color}2) {Colors.greed_color}hashcat -a 0 -m %NUM_OF_HASH your_hash.hash PATH_TO_YOUR_WORDLIST.dict"""

def getFraze(type_of_hash, HASH, num_of_hash):
    return fraze.replace('%HASH', HASH).replace('%TYPE_OF_HASH', str(type_of_hash)).replace('%NUM_OF_HASH', str(num_of_hash))

