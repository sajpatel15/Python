''' Module test_lab03.py '''
import pytest
from lab03 import problem_1, problem_2, problem_3, problem_4

def test_problem_1():
    result = problem_1(range(100), 8)
    assert result == [0, 8, 16, 24, 32, 40, 48,
                      56, 64, 72, 80, 88, 96]

def test_problem_2():
    result = problem_2(range(100), 4)
    assert result == [4, 14, 24, 34, 40, 41, 42, 43, 44, 45,
                      46, 47, 48, 49, 54, 64, 74, 84, 94]

def test_problem_3():
    result = problem_3('the quick brown fox jumped over the lazy dog', ['a', 'e', 'i', 'o', 'u'])
    assert result == 'th qck brwn fx jmpd vr th lzy dg'

def test_problem_4():
    result = problem_4(range(20, 50))
    assert result == [20, 21, 22, 24, 25, 26, 27, 28, 30, 32,
                      33, 34, 35, 36, 38, 39, 40, 42, 44, 45,
                      46, 48, 49]
