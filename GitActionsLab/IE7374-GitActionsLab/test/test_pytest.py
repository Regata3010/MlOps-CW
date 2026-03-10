import sys
sys.path.insert(0, 'src')
from calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(2, 3) == 6

def test_fun4():
    assert fun4(2, 3) == 10