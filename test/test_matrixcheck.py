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
    A = np.matrix([[1.000001, 0.000003], [0.000002, 2.00000099]])
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
    
def test_matrix_float_error():
    A = np.matrix([[3.0, 0.0], [0.0, 10.0]])
    with pytest.raises(Exception) as e_info:
        checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce');

def test_eq_matrix():
    A = np.matrix([[1.0, 0.0], [0.0, 2.0]])
    checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

def test_scalar_eq_matrix():
    A = np.matrix([[1, 0], [-0, 2]])
    A2 = np.matrix(2*A)
    checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

def test_swap_rows_eq_matrix():
    A = np.matrix([[0.0, 2.0],[1.0, 0.0]])
    checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

def test_swap_col_eq_matrix():
    A = np.matrix([[2.0, 0.0],[0.0, 1.0]])
    checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

def test_row_multiply_eq_matrix():
    A = np.matrix([[1.0, 0.0], [0.0, 2.0]])
    A = np.matrix([[4,0],[0,100]])*A
    checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

def test_non_square_eq_matrix():
    A = np.matrix([[1.0, 0.0, 2], [0.0, 2.0, 1]])
    checkanswer.eq_matrix(A, 'b975df4d16100051030dab90f432b14b')

def test_non_square_row_multiply_eq_matrix():
    A = np.matrix([[1.0, 0.0, 2], [0.0, 2.0, 1]])
    A = np.matrix([[4,0],[0,100]])*A
    checkanswer.eq_matrix(A, 'b975df4d16100051030dab90f432b14b')
        
def runall_matrix():
    test_matrix()
    test_matrix_roundoff()
    test_matrix_array()
    test_matrix_int()
    test_matrix_sympy()
    test_matrix_negative_zero()
    test_matrix_float_error()
    
if __name__ == "__main__":
    runall_matrix()
    