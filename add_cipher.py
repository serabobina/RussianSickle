import json
import os
import Dictionary
        

def getCommand(commands_list):
    command = 0
    while command == 0:
        number = input("\n>> Write command: ").strip()
        if number.isdigit():
            number = int(number)
        else:
            number = -1
            
        if 0 < number <= len(commands_list):
            command = commands_list[number - 1]
        else:
            print("Invalid command")
    return command

def printCommands(commands_list):
    print("\n+++ CIPHER +++")
    for i in range(len(commands_list)):
        print(f"{i + 1}) {commands_list[i]}")


def printCiphers(ciphers_dict):
    for cipher, rule in ciphers_dict.items():
        print(f'> {cipher}: {rule}\n')


def getTrueCipher():
    name = input("Write name of the cipher: ")
    length = getDigit("Write length of the cipher string: ")
    regular_string = input("Write regular string of the cipher string: ")
    group = input("Write group of the cipher: ")

    return (name, {"length": length, "regular_string": regular_string, "group": group})


def getDigit(fraze):
    while True:
        n = input(fraze)
        if checkDigit(n):
            return int(n)
        else:
            fraze = "Digit pls. Try again: "


def checkDigit(n: str):
    try:
        int(n)
    except:
        return 0
    return 1

    
def addCipher():
    new = getTrueCipher()

    Dictionary.add(new)


    

def exitCipher():
    print('Bye')

def getCipherName(ciphers):
    print("Avaible ciphers: ")
    printCiphers(Dictionary.get())

    fraze = "Name of the cipher: "
    while True:
        cipher = input(fraze)
        
        if cipher in Dictionary.get().keys():
            return cipher
        fraze = 'Error. Please try again: '
    

def deleteCipher():
    cipher = getCipherName(Dictionary.get())

    Dictionary.delete(cipher)
    print(cipher, 'deleted')

def printRaw(ciphers):
    print(ciphers)
    

        
def main():
    commands_dict = {"Print ciphers": lambda: printCiphers(Dictionary.get()),       #"Show commands": lambda : printCommands(list(commands_dict.keys()))
                     "Add cipher": addCipher,
                     "Delete cipher": deleteCipher,
                     "Print raw": lambda: printRaw(Dictionary.get()),
                     "Exit": exitCipher}
    commands_list = list(commands_dict.keys())
    
    printCommands(commands_list)

    while True:
        command = getCommand(commands_list)
        
        if command == "Exit":
            exitCipher()
            break
        

        commands_dict[command]()

        printCommands(commands_list)
    



if __name__ == '__main__':
    main()
