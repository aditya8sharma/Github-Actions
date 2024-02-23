def add(a,b):
    return a+b


# testing
def test_add():
    assert add(1,1) == 3
    assert add(1,-1) == 0
    assert add(1,-2) == -1
    assert add(43,33) == 76
