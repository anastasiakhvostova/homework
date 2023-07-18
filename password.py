print('Пароль повинен бути: '
      '1. Довжиною більше 8',
      '2. В паролі повинні бути Великі літери, маленькі літери, числа і спеціальний знак мінімум один з:('
      '+-/*!"№;%:?*()).'
      )
# my_password = (input(f'Ведіть пароль: '))
lowercase_letters = tuple("abcdefghijklmnopqrstuvwxyz")
# letters_big = ('АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯ')
# letters_small = ('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
uppercase_letters = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = tuple("0123456789")
symbols = '+-/*!"№;%:?*()'


def check_password(my_password) -> bool:
    numbers = 0
    uplatter = 0
    lowlatter = 0
    specsymbol = 0
    if len(my_password) >= 8:
        for mark in my_password:
            if mark in lowercase_letters:
                lowlatter += 1
            if mark in uppercase_letters:
                uplatter += 1
            if mark in digits:
                numbers += 1
            if mark in symbols:
                specsymbol += 1
    elif len(my_password) in range(0, 8):
        return False
    if lowlatter >= 1 and uplatter >= 1 and numbers >= 1 and specsymbol >= 1:
        return True
    else:
        return False


check_password()
