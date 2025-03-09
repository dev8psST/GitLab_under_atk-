import pytest
from add import add

def test_add():
    assert add(5,6) == 11
    assert add(34,6) == 40
    assert add(3.8,9)  == 12.8
    assert add("Hello","pytest")