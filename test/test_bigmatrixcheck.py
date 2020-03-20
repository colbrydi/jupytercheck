import random
import pytest
import numpy as np
import sympy as sym
from answercheck import checkanswer

def test_init():
    return True

def test_random_big_matrix():
    random.seed(20)
    A = np.empty((20,20))
    for i in range(20):
        for j in range(20):
            A[i][j] = random.randrange(100)
    # print(A)
    checkanswer.basic(A,"d19091cc42cf6db5f8e09d7564020b89")

def test_random_bigger_matrix():
    random.seed(50)
    A = np.empty((50,50))
    for i in range(50):
        for j in range(50):
            A[i][j] = random.randrange(100)
    checkanswer.basic(A, "5894d08ef2dfc6b7c9be2049f6459d29")

def test_random_hundred_matrix():
    random.seed(100)
    A = np.empty((100,100))
    for i in range(100):
        for j in range(100):
            A[i][j] = random.randrange(100)
    checkanswer.basic(A, "d0510719f5e646a51379c72269e94d2d")

def test_float_big_matrix():
    random.seed(20)
    A = np.empty((20,20))
    for i in range(20):
        for j in range(20):
            A[i][j] = random.random()
    # print(A)
    checkanswer.basic(A, "51147d5263bc91ed2822f3b6455e2d85")

def test_float_bigger_matrix():
    random.seed(50)
    A = np.empty((50,50))
    for i in range(50):
        for j in range(50):
            A[i][j] = random.random()
    # print(A)
    checkanswer.basic(A,"a7e01c1536cb00232f3288f283a5f93f")

def test_float_hundred_matrix():
    random.seed(100)
    A = np.empty((100,100))
    for i in range(100):
        for j in range(100):
            A[i][j] = random.random()
    # print(A)
    checkanswer.basic(A,"9d9493537ead212c66cd4a77dedcaec4")
    # checkanswer.basic(A,"9d9493537ead212c66cd4a77dedcaec4")