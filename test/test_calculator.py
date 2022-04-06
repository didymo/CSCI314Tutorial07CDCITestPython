import pytest
from Calculator import Calculator


# a successful test
def test_add():
    assert Calculator.add(5, 4) == 9


# an unsuccessful test.
def test_two():
    assert 4 == 5
