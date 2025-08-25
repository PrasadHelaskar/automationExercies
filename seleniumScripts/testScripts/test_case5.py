import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase5 import testCaseFive
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseFive():
    @pytest.mark.order(5)
    def test_caseFive(self,driver):
        initialTest().initialtest(driver)
        tcf=testCaseFive(driver)
        faker=Faker('en_US')
        startTime=time.time()
        name=faker.name()
        email="destiny99@example.net"
        log.info("name %s",name)
        log.info("email %s",email)
        tcf.signupActions(name,email)

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
