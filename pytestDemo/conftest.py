import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executed first")
    yield
    print("i will executed last")