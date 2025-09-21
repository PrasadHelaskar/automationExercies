import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase20 import testCaseTwenty
from seleniumScripts.testScripts.test_case12 import Test_caseTwelve as test12
from seleniumScripts.testScripts.test_case2and3 import Test_caseTwo as test2


log=Logger().get_logger(__name__)

class test12Helper(test12):
    __test__=False

class test2Helper(test2):
    __test__=False

class Test_caseTwenty():
    @pytest.mark.order(20)
    def test_caseTwenty(self,driver):
        initialTest().initialtest(driver)
        tct=testCaseTwenty(driver)
        startTime=time.time()
        tct.openProductPage()
        tct.verifyPageTitle()

        tct.searchActions() # verify pending
        test12Helper().test_caseTwelve(driver) # ammended test case 12 
        data={"email": "amanda14@example.com", "password": "123654789"}
        test2Helper().test_caseTwo(driver,data)

        tct.clickCartPage()

        script="""return document.querySelectorAll("[id*='product']").length;"""
        countFromWebpage=driver.execute_script(script)
        
        log.info("Count of Elements/Products: %s",countFromWebpage)
        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))