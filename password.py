lowercase_letters = tuple("abcdefghijklmnopqrstuvwxyz")
uppercase_letters = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = tuple("0123456789")
symbols = '+-/*!"№;%:?*()'


def check_password(my_password) -> bool:
    numbers = 0
    uppercase_latter = 0
    lowercase_latter = 0
    special_symbol = 0
    if len(my_password) >= 8:
        for mark in my_password:
            if mark in lowercase_letters:
                lowercase_latter += 1
            if mark in uppercase_letters:
                uppercase_latter += 1
            if mark in digits:
                numbers += 1
            if mark in symbols:
                special_symbol += 1
    elif len(my_password) in range(0, 8):
        return False
    if lowercase_latter >= 1 and uppercase_latter >= 1 and numbers >= 1 and special_symbol >= 1:
        return True
    else:
        return False
