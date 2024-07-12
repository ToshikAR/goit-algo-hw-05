'''
Розробіть Python-скрипт для аналізу файлів логів. 
Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, 
і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. 
Також користувач може вказати рівень логування як другий аргумент командного рядка, 
щоб отримати всі записи цього рівня.

'''
import sys
import os
import re
from colorama import Fore
from collections import Counter



def parse_log_line(line: str) -> dict:
    pattern = (r'(?P<date>\d{4}-\d{2}-\d{2})'
        + r' (?P<time>\d{2}:\d{2}:\d{2})'
        + r' (?P<level>[A-Z]+)'
        + r' (?P<msg>[A-z0-9 %]+)'
        )
    return re.match(pattern, line).groupdict()


def load_logs(file_path: str) -> list:
    logs = []
    if not os.path.exists(file_path):
        print(Fore.RED + f"File '{file_path}' does not exist" + Fore.RESET)
        return logs
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except Exception as e:
        print(Fore.RED + f"Error opening {file_path}:\n {e}" + Fore.RESET)
    
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return (list(filter(lambda log: log["level"] == level, logs)))


def count_logs_by_level(logs: list) -> dict:
    log_counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING":0}
    for log in logs:
        log_counts[log['level']] += 1

    return log_counts


def display_log_counts(counts: dict):
     base_format = '{:<18} | {:^11}'
     header = base_format.format('Рівень логування', 'Кількість' )
     divider = base_format.format('-'*18 , '-'*11)

     print(Fore.BLUE + '')
     print(header)
     print(divider)
     for level, quan in counts.items():
        print(base_format.format(level, quan))
     print('' + Fore.RESET)


def main(*argv):
    path = ''
    level = ''
    if len(sys.argv) == 1:
        path = r"Task3\task3.log"
    elif len(sys.argv) == 2:
        path = sys.argv[1]
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        level = sys.argv[2]
    else:
        print(f"There must be no more than 3 arguments")
        os.exit(1)


    if not path == '':
        level = level.upper()
        log_lines: list = load_logs(path)
        if len(log_lines) == 0: return
        display_log_counts(count_logs_by_level(log_lines))

    if not level == '':
        log_levels = filter_logs_by_level(log_lines, level)

        if not len(log_levels) == 0:
            print(Fore.BLUE + f"Деталі логів для рівня '{level}':")
            for level in log_levels:
                print(f"{level['date']} {level['time']} - {level['msg']}")
        else:
            print(Fore.RED + f"Деталі логів для рівня '{level}' не знайдено.")
        print('' + Fore.RESET)


if __name__ == "__main__":
    main(sys.argv)