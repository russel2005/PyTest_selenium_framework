import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.skip
def test_Greet_credit_card ():
    print("Good Morning")
