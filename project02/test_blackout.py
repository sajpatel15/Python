import pytest
from project02 import new_board, board_to_string, flip_cell, is_winning

def test_new_board():
    x = 4
    y = 5
    b = new_board(x, y)
    assert b == [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        ]

def test_board_to_string():
    b = [
        [False, True, True],
        [True, True, True],
        [False, False, False]
        ]
    s = board_to_string(b)
    assert s == 'O X X\nX X X\nO O O\n'

def test_flip_cell():
    b = [
        [False, True, True],
        [True, True, True],
        [False, False, False]
        ]
    flip_cell(b, 1, 1)
    assert b == [
        [False, False, True],
        [False, False, False],
        [False, True, False]
        ]

def test_is_winning():
    b = [
        [False, True, True],
        [True, True, True],
        [False, False, False]
        ]
    assert is_winning(b) == False
    b = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
        ]
    assert is_winning(b) == True
    b = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
        ]
    assert is_winning(b) == True
