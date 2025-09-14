import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase14 import testCaseFourteen
from seleniumScripts.testScripts.test_case13 import Test_caseThirteen as test13
from seleniumScripts.testScripts.test_case1 import Test_caseOne as test1


log=Logger().get_logger(__name__)
faker=Faker()

class test13Helper(test13):
    __test__=False

class test1Helper(test1):
    __test__=False


class Test_caseFourteen():
    @pytest.mark.order(6)
    def test_caseFourteen(self,driver):
        tcf=testCaseFourteen(driver)
        startTime=time.time()
        test13Helper().test_caseThirteen(driver)
        tcf.clickProceedCheckout()
        tcf.clickLoginButtonModel()
        test1Helper().test_caseOne(driver)
        tcf.clickCratButton()
        tcf.clickProceedCheckout()
        message=faker.paragraph(nb_sentences=1)
        tcf.enterMessage(message)
        tcf.clickPlaceOrder()

        tcf.removeRequiredtag()
        
        tcf.clickSubmitCard()
        time.sleep(6)
        tcf.postAccountActions()

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))