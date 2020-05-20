import pytest
import numpy as np
import sympy as sym
from answercheck import checkanswer

def test_init():
    return True

def test_vector():
    A = np.matrix([1.0, 0.0, 2.44])
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');
    
def test_vector_roundoff():
    A = np.matrix([[1.000001, 0.00000, 2.440000000234]])
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_array():
    A = [[1.0, 0.0, 2.44]]
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_array():
    A = sym.Matrix([1.0, 0.0, 2.44])
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_transpose():
    A = [[1.0], [0.0], [2.44]]
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_negative_zero():
    A = np.matrix([1.0, -0.0, 2.44])
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_negative_zero():
    A = np.matrix([1.0, -0.0, 2.44])
    checkanswer.vector(A, 'be281882fcabe04f0c880b70169814cd');

def test_vector_int():
    A = [1.0, 0.0, 2.0]
    checkanswer.eq_vector(A, '01ae20900734994659fa6cb57e3616ff');
    A = [1, 0, 2]
    checkanswer.eq_vector(A, '01ae20900734994659fa6cb57e3616ff');

def test_vector_sympy():
    A = sym.Matrix([[1.0, 0.0, 2.0]])
    checkanswer.eq_vector(A, '01ae20900734994659fa6cb57e3616ff');
    
def test_vector_float_error():
    A = np.matrix([[3.0, 0.0, 0.0, 10.0]])
    with pytest.raises(Exception) as e_info:
        checkanswer.eq_vector(f, '943d90b283d21136da008160e002a5ce');

def runall_vectors():
    test_vector()
    test_vector_roundoff()
    test_vector_array()
    test_vector_transpose()
    test_vector_int()
    test_vector_sympy()
    test_vector_negative_zero()
    test_vector_float_error()
    
if __name__ == "__main__":
    runall_vectors()
    
