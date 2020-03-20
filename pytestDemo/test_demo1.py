import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.skip
def test_Greet_credit_card ():
    print("Good Morning")


@pytest.mark.smoke
def test_open_file():
    try:
        f = open("test.txt", encoding='utf-8')
        # perform file operations
    finally:
        f.close()