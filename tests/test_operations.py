from src.operations import add , sub,mult 


def test_add_operation():
    assert add(2,5)==7
    assert add(2,99)==101
    assert add(2,0)==2

def test_sub_operations():
    assert sub(3,3)==1

def test_multi_operations():
    assert mult(3,9)==27