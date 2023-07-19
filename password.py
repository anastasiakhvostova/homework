from string import ascii_lowercase, ascii_uppercase, digits
symbols = '+-/*!"№;%:?*()'


def are_lowercase_letter(my_password: str) -> bool:
    for mark in my_password:
        if mark in ascii_lowercase:
            return True


def are_uppercase_letter(my_password: str) -> bool:
    for mark in my_password:
        if mark in ascii_uppercase:
            return True


def are_digits(my_password: str) -> bool:
    for mark in my_password:
        if mark in digits:
            return True


def are_symbol(my_password: str) -> bool:
    for mark in my_password:
        if mark in symbols:
            return True


def is_password_correct(my_password: str) -> bool:
    d = are_symbol(my_password), are_digits(my_password), are_lowercase_letter(my_password), are_uppercase_letter(my_password)
    if len(my_password) >= 8:
        return all(d)
    else:
        return False
