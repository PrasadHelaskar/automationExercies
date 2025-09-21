import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase25 import testCaseTwentyFive

log=Logger().get_logger(__name__)
faker=Faker()

class Test_caseTwentyFive():
    @pytest.mark.order(25)
    def test_caseTwentyFive(self,driver):
        tctf=testCaseTwentyFive(driver)
        initialTest().initialtest(driver)
        startTime=time.time()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        assert tctf.getBottomSubscriptionTitleText().lower() == "Subscription".lower() , "Botton title didn't match"

        tctf.clickScrollToTOp()

        assert tctf.getTextForTopTitle().lower() == "Full-Fledged practice website for Automation Engineers".lower() , "Top title didn't match"

        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))