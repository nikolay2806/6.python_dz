from venv import *
from python import *

def test_py_pow():
        assert py_pow(2, 2) == 4
        assert py_pow(3, 3) == 27
        assert py_pow(4, 4) == 256


def test_py_sqrt():
        assert py_sqrt(9) == 3.0
        assert py_sqrt(16) == 4.0
        assert py_sqrt(25) == 5.0

def test_py_pi():
      assert py_pi(3.141592653589793) == True

def test_py_hypot():
        assert py_hypot(10, 3) == 10
        assert py_hypot(10, 5) == 11

def test_py_hypot():
        assert py_hypot(10, 3) == 10
        assert py_hypot(10, 5) == 11

def test_out_filter():
        assert out_filter([1,2,4,5,7,8,10,11]) == [2,4,8,10]