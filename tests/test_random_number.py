import random_number
import pytest
import random


number = random.randint(0, 1000)
my_number = [(number < 0, False), (number > 1000, False)]


@pytest.mark.parametrize('value, result', my_number)
def test_password(value, result):
    assert random_number.have_random_number(value) == result
