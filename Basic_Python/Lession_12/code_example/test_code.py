from ctypes import util
from re import U
from code_example import calc, util

def test_calc():
    cals = Cals()
    imput = [1, 3, 4, 5]
    assert cals.sum(input)
