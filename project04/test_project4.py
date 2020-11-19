'''Module test_project04.py'''
import pytest
from project04 import cypher_alphabet, encrypt, get_unencrypted_text

def test_cypher_alphabets():
    text = "motherboard"
    assert cypher_alphabet(text) == "motherbadcfgijklnpqsuvwxyz"
    assert len(cypher_alphabet(text)) == 26

def test_encrypt():
    text = "This is a file. This file has some WORDS in it."
    cypher_alphabet = "motherbadcfgijklnpqsuvwxyz"
    assert encrypt(text, cypher_alphabet) == "Sadq dq m rdge. Sadq rdge amq qkie WKPHQ dj ds."
    assert not encrypt(text, cypher_alphabet) == "sadq dq m rdge. sadq rdge amq qkie wkphq dj ds."

def test_get_unencrypted_text():
    file_path = "text.txt"
    assert get_unencrypted_text(file_path) == "This is a file. This file has some WORDS in it. This file is named text.\n"
    assert not get_unencrypted_text(file_path) == "This is a file. This file has some WORDS in it."
    assert not len(get_unencrypted_text(file_path)) == 20
