import time
import pytest
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase9 import testCaseNine
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseNine():
    @pytest.mark.order(6)
    def test_caseNine(self,driver):
        initialTest().initialtest(driver)
        tcn=testCaseNine(driver)
        startTime=time.time()
        tcn.visitProductDetailsPage()

        productName="women"
        tcn.enterProductDesciption(productName)

        productNames=tcn.getAllProductNames()

        if not any(productName.lower() in name.lower() for name in productNames):
            tcn.DD(productNames)

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
