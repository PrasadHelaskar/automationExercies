import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase10 import testCaseTen
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseTen():
    @pytest.mark.order(6)
    def test_caseTen(self,driver):
        initialTest().initialtest(driver)
        tct=testCaseTen(driver)
        startTime=time.time()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        tct.subscriptionEnrollment(Faker('en_US').email())
        
        message=tct.successMessageVerfity()

        if not message=="You have been successfully subscribed!":
            tct.DD(message)
            
        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
