import pytest
import numpy as np
import sympy as sym
from answercheck import checkanswer

def test_init():
    return True

def test_matrix():
    A = np.matrix([[1.0, 0.0], [0.0, 2.0]])
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');
    
def test_matrix_roundoff():
    A = np.matrix([[1.000001, 0.000003], [0.000002, 2.0000099]])
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');

def test_matrix_array():
    A = [[1.0, 0.0], [0.0, 2.0]]
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');
    
def test_matrix_int():
    A = [[1, 0], [0, 2]]
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');
    
def test_matrix_sympy():
    A = sym.Matrix([[1, 0], [0, 2]])
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');

def test_matrix_negative_zero():
    A = np.matrix([[1.0, -0.0], [-0.0, 2.0]])
    checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');
    
def test_matrix_error():
    A = np.matrix([[3.0, 0.0], [0.0, 10.0]])
    with pytest.raises(Exception) as e_info:
        checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');


    