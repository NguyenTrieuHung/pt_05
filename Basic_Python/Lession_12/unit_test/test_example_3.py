#input value for pytest
# run pytest -k 

import pytest

#@pytest.fixture
#def input_value():
#    input = 34
#    return input

def test_divisiable_by_3(input_value):
    assert input_value % 3 == 0

def test_divisiable_by_5(input_value):
    assert input_value % 5 == 0