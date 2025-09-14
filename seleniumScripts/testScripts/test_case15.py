import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase15 import testCaseFifteen
from seleniumScripts.testScripts.test_case13 import Test_caseThirteen as test13
from seleniumScripts.testScripts.test_case1 import Test_caseOne as test1


log=Logger().get_logger(__name__)
faker=Faker()

class test13Helper(test13):
    __test__=False

class test1Helper(test1):
    __test__=False


class Test_caseFifteen():
    @pytest.mark.order(6)
    def test_caseFifteen(self,driver):
        tcf=testCaseFifteen(driver)
        startTime=time.time()
        test1Helper().test_caseOne(driver)
        test13Helper().test_caseThirteen(driver)
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