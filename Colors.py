from colorama import *

default_color = Style.RESET_ALL + Fore.YELLOW
options_color = Style.RESET_ALL + Fore.LIGHTMAGENTA_EX
error_color = Style.RESET_ALL + Fore.RED
decode_color = Style.RESET_ALL + Fore.BLUE + Style.BRIGHT
user_input_color = Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW
question_color = Style.RESET_ALL + Fore.YELLOW
greed_color = Style.RESET_ALL + Fore.LIGHTCYAN_EX + Style.BRIGHT
author_color = Style.RESET_ALL + Fore.GREEN + Style.BRIGHT

default_pref = default_color + '[*] '
decode_pref = decode_color + '[+] '
error_pref = error_color + '[!] '
question_pref = question_color + '[?] '
about_pref = greed_color + ''
string_not_found_pref = error_color + '[-] '
