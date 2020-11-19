import time
from socket import *
import pytest
from lab07 import HighCardServer

def test_server():
    h1 = HighCardServer("localhost", 9000, 1)
    h2 = HighCardServer("localhost", 9001, 1)

    h1.start_server()
    assert True # ensure non-blocking server

    h2.start_server()
    assert True # ensure non-blocking server

    s = socket()
    s.connect(("localhost", 9000))
    
    time.sleep(1) # wait to make sure we get all the responses

    data = s.recv(2048)
    string = data.decode()
    assert "Hello, welcome to" in string
    assert "The dealer has" in string
    assert "You have" in string
    assert "win" in string.lower() or "tie" in string.lower()

    s2 = socket()
    s2.connect(("localhost", 9001))

    time.sleep(1) # wait to make sure we get all the responses

    data2 = s2.recv(2048)
    string2 = data2.decode()
    assert "Hello, welcome to" in string2
    assert "The dealer has" in string2
    assert "You have" in string2
    assert "win" in string2.lower() or "tie" in string2.lower()
