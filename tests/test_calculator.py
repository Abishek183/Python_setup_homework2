'''Testing the calculator class'''
from calculator import calculator

def test_calculator():
    '''Testing the calculator methods'''
    assert calculator.add(2,2) == 4
    assert calculator.subtract(2,2) == 0
    assert calculator.multiply(2,3) == 6
    assert calculator.divide(2,2) == 1
