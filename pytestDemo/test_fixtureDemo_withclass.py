# setup method is invoked from conftest.py
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixture_demo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixture_demo3(self):
        print("i will execute steps in fixtureDemo3 method")

