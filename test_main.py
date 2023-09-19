from main import *


## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2

  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10 * 10
  assert quadratic_multiply(BinaryNumber(30), BinaryNumber(35)) == 30 * 35
  assert quadratic_multiply(BinaryNumber(200), BinaryNumber(210)) == 200 * 210
