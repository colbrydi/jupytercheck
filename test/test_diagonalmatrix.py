import random
import pytest
import numpy as np
import sympy as sym
from answercheck import checkanswer


def test_float_diagonal_fromzeros_matrix():
    random.seed(200)
    A = np.zeros((100,100))
    for i in range(100):
        A[i][i] = random.random()
    checkanswer.basic(A,"4bb7fffaab2310b50b28c65fd3909b34")


# THIS WILL NOT WORK
'''
def test_float_diagonal_fromempty_matrix():
    random.seed(200)
    A = np.empty((100,100))
    for i in range(100):
        A[i][i] = random.random()
    checkanswer.basic(A)
'''

def test_np_diag_matrix():
    random.seed(400)
    random_list = [random.random() for i in range(30)]
    A = np.diag(random_list)
    checkanswer.basic(A,"7614e2daaf3df99dbb48b02ada83ef9a")

def test_big_np_diag_matrix():
    random.seed(400)
    random_list = [random.random() for i in range(80)]
    A = np.diag(random_list)
    checkanswer.basic(A,"28e092a7de0b446c0eeff65e14a9a297")