import pytest
import password


my_password = [('nasTya9-', True),
               ('nastya9+', False),
               ('NASTYA7-', False),
               ('NAStYA-+', False),
               ('NAStYa876', False),
               ('nAst8-', False)]


@pytest.mark.parametrize('value, result', my_password)
def test_password(value, result):
    assert password.is_password_correct(value) is result
