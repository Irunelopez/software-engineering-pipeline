from calculator import add, multiply, square, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_square():
    assert square(2) == 4
    assert square(5) == 25  # Fixed the typo from main!