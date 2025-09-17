import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase16 import testCaseSixteen
from seleniumScripts.testScripts.test_case13 import Test_caseThirteen as test13
from seleniumScripts.testScripts.test_case1 import Test_caseOne as test1
from seleniumScripts.testScripts.test_case2and3 import Test_caseTwo as test2


log=Logger().get_logger(__name__)
faker=Faker()

class test13Helper(test13):
    __test__=False

class test1Helper(test1):
    __test__=False

class test2Helper(test2):
    __test__=False

#check the text cases 1,2,13 for successful exexution need alteratiom 

class Test_caseFifteen():
    @pytest.mark.order(6)
    def test_caseSixteen(self,driver):
        tcs=testCaseSixteen(driver)
        startTime=time.time()
        data={"email": "your.email+fakedata98129123@gmail.com", "password": "123654789"}
        test1Helper().test_caseOne(driver)
        tcs.clicklogoutButton()
        test2Helper().test_caseTwo(driver,data)
        test13Helper().test_caseThirteen(driver)
        tcs.clickProceedCheckout()
        message=faker.paragraph(nb_sentences=1)
        tcs.enterMessage(message)
        tcs.clickPlaceOrder()

        tcs.removeRequiredtag()
        
        tcs.clickSubmitCard()
        time.sleep(6)
        tcs.postAccountActions()

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))