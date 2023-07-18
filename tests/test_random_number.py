import random_number
import random


number = random.randint(0, 1000)


def test_random_number():
    if number > 1000:
        return False


test_random_number()
