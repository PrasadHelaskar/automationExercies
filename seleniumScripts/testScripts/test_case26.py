import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase26 import testCaseTwentySix

log=Logger().get_logger(__name__)
faker=Faker()

class Test_caseTwentySix():
    @pytest.mark.order(26)
    def test_caseTwentySix(self,driver):
        tcts=testCaseTwentySix(driver)
        initialTest().initialtest(driver)
        startTime=time.time()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        assert tcts.getBottomSubscriptionTitleText().lower() == "Subscription".lower() , "Botton title didn't match"

        driver.execute_script("window.scrollTo(0, 0)")

        assert tcts.getTextForTopTitle().lower() == "Full-Fledged practice website for Automation Engineers".lower() , "Top title didn't match"

        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))