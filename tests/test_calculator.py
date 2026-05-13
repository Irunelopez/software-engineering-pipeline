from calculator import add, sub, divide


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


<<<<<<< feature/multiply
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
=======
def test_divide():
    assert divide(6, 2) == 3
    assert divide(8, 4) == 2
>>>>>>> main
