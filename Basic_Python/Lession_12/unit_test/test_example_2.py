import os

import pytest

def test_greater():
    num = 200
    assert num > 20

def test_less():
    num = 30
    assert num > 30
#pytest
#pytest -k greater -v test rieng greater
