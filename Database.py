import json
import os
from datetime import datetime
import config

base_dir_path = config.DIR_PATH + 'database'
base_file_path = 'database.json'
base_path = f'{base_dir_path}/{base_file_path}'


def get():
    createIfNotExist()
    with open(base_path) as file:
        return json.load(file)


def save(new_reports: dict):
    createIfNotExist()
    with open(base_path) as file:
        reports = json.load(file)

    for string in new_reports.keys():
        string_name = getUniqueString(string, reports.keys())
        reports[string_name] = {'value': string,
                                'time': getTime(), 'result': new_reports[string]}

    with open(base_path, 'w') as file:
        json.dump(reports, file)


def clear():
    with open(base_path, 'w') as file:
        file.write('{}')


def delete(report_name):
    with open(base_path) as file:
        reports = json.load(file)

    if report_name in reports:
        del reports[report_name]

    with open(base_path, 'w') as file:
        json.dump(reports, file)


def getUniqueString(string, reports):
    pref = 2
    string_name = string
    while string_name in reports:
        string_name = string + f'({pref})'
        pref += 1
    return string_name


def createIfNotExist():
    if not os.path.isdir(base_dir_path):
        os.mkdir(base_dir_path)

    if not os.path.isfile(base_path):
        clear()


def getTime():
    report_time = datetime.now()

    year = report_time.year
    month = completeNulls(report_time.month, 2)
    day = completeNulls(report_time.day, 2)

    hour = completeNulls(report_time.hour, 2)
    minute = completeNulls(report_time.minute, 2)
    second = completeNulls(report_time.second, 2)

    return f'{year}.{month}.{day} {hour}:{minute}:{second}'


def completeNulls(num, length):
    return '0' * (len(str(num)) < length) + str(num)
