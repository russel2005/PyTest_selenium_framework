import pytest


@pytest.fixture()
def setup():
    print("i will be executed first")
    yield
    print("i will executed last")


# above code should be in conftest.py

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")