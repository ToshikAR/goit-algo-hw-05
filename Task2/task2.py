'''
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, 
ідентифікувати всі дійсні числа, що вважаються частинами доходів, і 
повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
чітко відокремлені пробілами з обох боків. Також потрібно реалізувати 
функцію sum_profit, яка буде використовувати generator_numbers для підсумовування 
цих чисел і обчислення загального прибутку.

'''
import re
from typing import Callable


def sum_profit(text: str, func: Callable) -> int:
    sum = 0
    gen = func(text)
    for num in gen:
        sum += num 
    return sum

def generator_numbers(text: str):
    numbers = re.findall(r'\d+.\d+', text)
    for number in numbers:
        yield float(number)


text = '''
Загальний дохід працівника складається з декількох частин: 1000.01 
як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.
'''
total = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total}.")
