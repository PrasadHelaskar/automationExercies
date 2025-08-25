import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase6 import testCaseSix
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseSix():
    @pytest.mark.order(6)
    def test_caseSix(self,driver):
        initialTest().initialtest(driver)
        tcs=testCaseSix(driver)
        faker=Faker('en_US')
        startTime=time.time()
        name=faker.name()
        email=faker.email()
        subject=faker.sentence()
        message=faker.paragraph()
        tcs.openContactUsPage()
        tcs.formFill(name,email,subject,message)
        driver.switch_to.alert.accept()
        tcs.messageSentConfirmation()

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
