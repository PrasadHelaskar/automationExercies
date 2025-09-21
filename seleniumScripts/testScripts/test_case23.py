import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase23 import testCaseTwentyThree
from seleniumScripts.testScripts.test_case1 import Test_caseOne as test1
from seleniumScripts.testScripts.test_case13 import Test_caseThirteen as test13

log=Logger().get_logger(__name__)
faker=Faker()

class test1Helper(test1):
    __test__=False

class test13Helper(test13):
    __test__=False

class Test_caseTwentyThree():
    @pytest.mark.order(23)
    def test_caseTwentyThree(self,driver):
        tctt=testCaseTwentyThree(driver)
        startTime=time.time()
        data=test1Helper().test_caseOne(driver=driver)
        
        fianlAddress=data.get("address").split("\n")[0]+" "+data.get("city")+" "+data.get("state")+" "+data.get("zipCode")
        
        test13Helper().test_caseThirteen(driver=driver)

        tctt.clickProceedToCheckoutButton()

        assert tctt.deliveryAddress().lower() == fianlAddress.lower(), "Address didn't match"
        
        assert tctt.bilingAddress().lower() == fianlAddress.lower(), "Address didn't match"

        tctt.postAccountActions()
        
        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))