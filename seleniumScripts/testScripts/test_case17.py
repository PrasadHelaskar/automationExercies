import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_case13 import Test_caseThirteen as test13
from seleniumScripts.pageObjects.testCase17 import testCaseSeventeen 

log=Logger().get_logger(__name__)

class test13Helper(test13):
    __test__=False

class Test_caseSeventeen():
    @pytest.mark.order(17)
    def test_caseSeventeen(self,driver):
        tcs=testCaseSeventeen(driver)
        startTime=time.time()
        test13Helper().test_caseThirteen(driver)
        tcs.clickCrossButton()
        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))