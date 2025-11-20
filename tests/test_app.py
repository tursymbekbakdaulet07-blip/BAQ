from app  import add
from app import div
def test_add():
  assert add(2, 3) == 5

def test_div():
  assert div(10, 5) == 2
