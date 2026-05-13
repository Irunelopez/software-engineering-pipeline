from calculator import add, sub
def test_add():
  assert add(2, 3) == 5
def test_sub():
  assert sub(10, 4) == 6

def test_divide():
  assert divide(6, 3) == 2
  assert divide(8, 2) == 4
