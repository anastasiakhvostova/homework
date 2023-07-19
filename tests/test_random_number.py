import random_number


def test_password():
    assert 0 < random_number.have_random_number() <= 1000
