import pytest
from pytestDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataload")
class TestDataDriven(BaseClass):

    def test_edit_profile(self, dataload):
        log = self.get_logger()
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload[2])


