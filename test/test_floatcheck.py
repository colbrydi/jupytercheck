import pytest
import numpy as np
import sympy as sym
from answercheck import checkanswer

def test_init():
    return True

def test_float():
    f = 0.0111
    checkanswer.float(f, '2e55d74f5c78981f6b877b198bdc61ba');
    
def test_float_roundoff():
    f = 0.011100001
    checkanswer.float(f, '2e55d74f5c78981f6b877b198bdc61ba');

def test_float_array():
    f = [[0.0111]]
    checkanswer.float(f, '2e55d74f5c78981f6b877b198bdc61ba');
    
def test_float_int():
    f = 1
    checkanswer.float(f, 'e4c2e8edac362acab7123654b9e73432');

def test_float_zero():
    f = 0.00
    checkanswer.float(f, '30565a8911a6bb487e3745c0ea3c8224');
    
def test_float_negative_zero():
    f = -0.00
    checkanswer.float(f, '30565a8911a6bb487e3745c0ea3c8224');
    
def test_float_error():
    f = 4.0
    with pytest.raises(Exception) as e_info:
        checkanswer.float(f, '2e55d74f5c78981f6b877b198bdc61ba');


    