'''
Модуль обробки контактів
'''
import re
from colorama import Fore, Style


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            return 'Phone number is incorrect.'
    return inner


def is_phone_number(phone) -> tuple[bool, str]:
    phone_number = re.sub(r"[^0-9]", "", phone)
    if not re.search(r'\d{10}$', phone_number):
        return False, phone
    else:
        phone = re.search(r'\d{10}$', phone_number)[0]
        return True, phone
    

@input_error
def add_contact(args, contacts):
    name, phone = args
    is_phon, num_phon = is_phone_number(phone)
    if not is_phon: raise IndexError()
    contacts[name] = num_phon
    return "Contact added."    


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name not in contacts: raise KeyError()
    is_phon, num_phon = is_phone_number(phone)
    if not is_phon: raise IndexError()
    contacts[name] = num_phon
    return "Contact change."

@input_error
def get_contact(args: list, contacts: dict) -> str:
    name = args[0]
    if name not in contacts: raise KeyError()
    return f"{name}: {contacts[name]}"


@input_error
def all_contact(contacts: dict) -> str:
    if len(contacts) == 0: return f"Container is empty"
    all = ''
    for name, phone in contacts.items():
        all += f"{name}: {phone}\n"
    return all.strip()
