import pytest


def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string not match."

@pytest.mark.smoke
def test_second_program():
    a = 6
    b = 4
    assert a+b == 10, "add program not working"
