import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase24 import testCaseTwentyFour
from seleniumScripts.testScripts.test_case15 import Test_caseFifteen as test15

log=Logger().get_logger(__name__)
faker=Faker()

class test15Helper(test15):
    __test__=False

class Test_caseTwentyFour():
    @pytest.mark.order(24)
    def test_caseTwentyFour(self,driver):
        tctf=testCaseTwentyFour(driver)
        startTime=time.time()
        
        test15Helper().test_caseFifteen(driver)

        tctf.downloadInvoice()

        tctf.postAccountActions()

        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))