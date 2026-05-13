from calculator import add, sub, modulo


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(8, 4) == 0

