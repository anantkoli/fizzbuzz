import pytest
from app.program import AppFizzBuzz


@pytest.fixture
def app() -> AppFizzBuzz:
    params = {'num1': 3, 'num2': 5, 'num_range': 10, 'word1': 'fizz', 'word2': 'buzz'}
    return AppFizzBuzz(params)


def test_app_creation(app: AppFizzBuzz):
    assert app.val_1 == 3
    assert app.word_1 == 'fizz'
    assert app.word_2 == 'buzz'
    assert app.num_range == 10
    assert type(app.num_range) == int

@pytest.mark.parametrize('params',
                         [{'num1': 3, 'num2': 5, 'num_range': 10, 'word1': 'fizz', 'word2': 'buzz'}]
                         )
def test_fizz_buzz_program(params):
    o = AppFizzBuzz(params)
    resp = o.run()
    assert resp == get_exp_resp(1)


def get_exp_resp( result):
    if result == 1:
        return ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']
