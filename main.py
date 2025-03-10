import pytest
from add import *

#add comment
def test_add_1():
    assert add(5,6) == 11
    
    assert add(3.8,9)  == 12.8
    

def test_add_2():
    assert add(34,6) == 40

def test_add_3():
    assert add("Hello"," pytest") == "Hello pytest"

