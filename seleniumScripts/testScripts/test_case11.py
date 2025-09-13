import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase11 import testCaseEleven
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseEleven():
    @pytest.mark.order(6)
    def test_caseEleven(self,driver):
        initialTest().initialtest(driver)
        tce=testCaseEleven(driver)
        startTime=time.time()
        
        tce.gotoCartPage()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        tce.subscriptionEnrollmentCartPage(Faker('en_US').email())
        
        message=tce.successMessageVerfity()

        if not message=="You have been successfully subscribed!":
            tce.DD(message)
            
        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))