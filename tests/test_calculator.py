from calculator import add, sub, truncate, multiply, modulo, divide, squared


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6

def test_truncate():
    assert truncate(3.9) == 3

def test_sqaured():
    assert squared(2) == 4
    
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_divide():
    assert multiply(6, 2) == 3
    assert multiply(8, 4) == 2

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(8, 4) == 0
