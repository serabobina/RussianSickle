import os
import json
import time
from colorama import init, ansi
from art import *
import Cracker
import Database
import Colors
import Signal
import argparse


init(autoreset=True)


def printResult(string, answer):

    print('\n' + Colors.default_pref + "String: " +
          Colors.greed_color + string, end='')

    for cipher, result in answer.items():
        state, pref, color = getStateAndPref(result, cipher)

        print('\n' + pref + cipher + state + color + result["result"])

    if len(answer) == 0:
        print('\n' + Colors.string_not_found_pref + "String not found :(\n")


def getStateAndPref(result, cipher):
    state = ' ' + "Cracked: "
    pref = Colors.decode_pref
    color = Colors.greed_color

    if result["group"] == 'bruteforce':
        state = ':\n'
        color = ''

    if result["group"] == 'hash':
        state = ': '
        color = ''

    if result["error"]:
        state = ' ' + "Error: "
        pref = Colors.error_pref
        color = Colors.error_color

    return (state, pref, color)


def ask(question, true_value='yes', false_value='no'):
    fraze = '\n' + Colors.question_pref + \
        f"{question} [{true_value}]/[{false_value}]: "

    while True:
        ans = input(fraze + Colors.user_input_color).lower()
        if ans == true_value:
            return 1
        elif ans == false_value:
            return 0
        else:
            fraze = Colors.error_pref + "Unrecognized input. Pls try again: "


def greeding():
    clearConsole()

    greed_fraze = text2art('RUSSIAN SICKLE', 'tarty1')

    print(Colors.greed_color + greed_fraze + '\n')


def clearConsole():
    print(ansi.clear_screen(), end='')
    print(ansi.Cursor.POS(), end='')


def printModes(modes):
    print(Colors.default_pref + "Modes: ")

    for i in range(len(modes)):
        print(Colors.options_color + f'{i+1}) {modes[i]}', end='  ')
    print()


def getElement(fraze, elements, fraze_to_exit='exit'):
    fraze = Colors.default_pref + fraze + ' '

    while True:
        print(fraze, end='')
        number_element = input(Colors.user_input_color)

        if number_element.strip().lower() == fraze_to_exit:
            return 0

        if not number_element.isdigit():
            fraze = Colors.error_pref + 'Error! Input must be number. Try again: '
            continue

        if not (1 <= int(number_element) and int(number_element) <= len(elements)):
            fraze = Colors.error_pref + 'Error! Number not in the right range. Try again: '
            continue

        return elements[int(number_element) - 1]


def exitToMenu():
    print('\n' + Colors.default_pref +
          'Press enter to exit... ', end='')
    input()


def CrackString():
    print(Colors.greed_color + '\n' + text2art("CRACKING", font='small'), end='')

    string = input(Colors.default_pref +
                   'Enter string you want to crack: ' + Colors.user_input_color)
    answer = Cracker.cracker(string, 0)

    printResult(string, answer)

    if askForSaveReport():
        saveReport(string, answer)
        print(Colors.default_pref + 'Saved!')

    exitToMenu()


def saveReport(string, result):
    Database.save({string: result})


def saveReportInFile(report, path):
    with open(path, 'w') as file:
        json.dump(report, file)


def askForSaveReport():
    question = 'Do you want to save report?'
    return ask(question)


def printDatabase():
    print(Colors.greed_color + '\n' + text2art("DATABASE", font='small'), end='')

    reports = Database.get()
    strings = list(reports.keys())
    print(Colors.default_pref + 'Reports: ')

    if len(reports) == 0:
        print(Colors.error_pref + "You have no saved reports.")
        exitToMenu()
        return

    count = 1
    for string_name in reports.keys():
        print(Colors.greed_color + f'{count}) {string_name}' +
              Colors.default_color + ' ' * 6 + f'{reports[string_name]["time"]}')
        count += 1
    print()

    fraze = "Enter number of element you want to see ('exit' to exit):"
    report_name = getElement(fraze, strings)

    if not report_name:
        return

    report = reports[report_name]

    clearConsole()

    printReport(report)

    if askForDeleteReport():
        deleteReport(report_name)
        print(Colors.default_pref + 'Deleted!')

    exitToMenu()


def printReport(report):
    string = report['value']
    time = report['time']

    print('\n' + Colors.default_pref + '>>> ' + time)

    printResult(string, report['result'])


def askForDeleteReport():
    fraze = 'Do you want to delete report?'
    return ask(fraze)


def deleteReport(report_name):
    Database.delete(report_name)


def About():
    print(Colors.greed_color + '\n' + text2art("ABOUT", font='small'), end='')

    thanks = ['Man1', 'Man2', 'Man3']
    author = 'serabobina'
    text = f'The Russian Sickle project allows you to crack encrypted strings, determine a possible hashing algorithm, and give recommendations on brute forcing hashed passwords. Russian Sickle knows 6 types of encryption, such as Base64, Caesar, Rail Fence ciphers, as well as Hexedimical, Binary, ASCII encodings, and others. Author: {Colors.author_color + author}{Colors.greed_color}. \nThanks: '

    for guy in thanks:
        text += Colors.author_color + '\n ' + guy

    text += Colors.greed_color + '\n\nLove you :)'

    print(Colors.greed_color + text)

    exitToMenu()


def exiting():
    print('\n' + Colors.default_pref + 'Seems like you want to exit. Bye!')
    exit()


def BruteForceString():
    print(Colors.greed_color + '\n' +
          text2art("BRUTE FORCING", font='small'), end='')

    string = input(Colors.default_pref +
                   'Enter string you want to brute force: ' + Colors.user_input_color)
    answer = Cracker.cracker(string, 1)

    printResult(string, answer)

    if askForSaveReport():
        saveReport(string, answer)
        print(Colors.default_pref + 'Saved!')

    exitToMenu()


def default_mode():
    modes = {"Crack string": CrackString,
             "Brute force string": BruteForceString,
             "Database": printDatabase, "About": About, "Exit": exiting}
    modes_keys = list(modes.keys())

    while True:
        greeding()

        printModes(modes_keys)
        print()
        mode = getElement(
            'Please enter number of mode you need to use:', modes_keys)

        func = modes[mode]
        func()


def get_strings_for_file(path):
    if not os.path.isfile(path):
        return 0

    with open(path) as file:
        return list(map(str.strip, file.readlines()))


def RussianSickle():
    parser = argparse.ArgumentParser(
        description='Cracking strings with RussianSickle.')

    parser.add_argument('-b', '--bruteforce', action='store_true',
                        help='A mode that allows you to crack a string using brute force using simple ciphers.')

    parser.add_argument(
        '-o', '--output', help='Path to output file (format: json).')

    parser.add_argument(
        '-i', '--input', help='Path to input file (format: each string on a new line).')

    parser.add_argument('-s', '--string', nargs='+',
                        help='String or strings for cracking.')

    parser.add_argument('-d', '--database', action='store_true',
                        help='Save report in database.')

    args = parser.parse_args()

    is_bruteforce_mode = args.bruteforce
    output_file = args.output
    input_file = args.input
    strings = args.string
    database_save = args.database

    if any((is_bruteforce_mode, output_file, input_file, strings)):
        greeding()
    else:
        default_mode()

    if input_file and strings:
        print(Colors.error_pref +
              "You must use --string and --input separately, not at the same time")

    reports = {}

    if strings:
        for string in strings:
            answer = Cracker.cracker(
                string, mode=is_bruteforce_mode, beautiful_print=0)
            reports[string] = answer

    if input_file:
        strings = get_strings_for_file(input_file)
        if not strings:
            print(Colors.error_pref + "File doesn't exist.")

        for string in strings:
            answer = Cracker.cracker(
                string, mode=is_bruteforce_mode, beautiful_print=0)
            reports[string] = answer

    if len(reports) > 0:
        if output_file:
            saveReportInFile(reports, output_file)

        if database_save:
            Database.save(reports)

        for string in reports:
            printResult(string, reports[string])

    else:
        BruteForceString()


def main():
    RussianSickle()


if __name__ == '__main__':
    main()
