from app  import add
from app import div
from app import mul
def test_add():
  assert add(2, 3) == 5

def test_div():
  assert div(10, 5) == 2

def test_mul():
  assert mul(12, 10) == 120
