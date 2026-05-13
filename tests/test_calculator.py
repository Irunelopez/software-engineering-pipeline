from calculator import add, sub
def test_add():
  assert add(2, 3) == 5
def test_sub():
  assert sub(10, 4) == 6

def test_square():
    assert square(2) == 4
    assert multiply(5) == 25
