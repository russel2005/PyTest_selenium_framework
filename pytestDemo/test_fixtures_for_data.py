import pytest


@pytest.mark.usefixtures("dataload")
class TestDataDriven:

    def edit_profile(self, dataload):
        print(dataload)
        print(dataload[0])
        print(dataload[2])


