from nin.mod1 import foo

def test_foo():
  assert foo(1) == 2

def test_bad():
  assert foo(2) == 2
