import time
import pytest
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase7 import testCaseSeven
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseSeven():
    @pytest.mark.order(7)
    def test_caseSeven(self,driver):
        initialTest().initialtest(driver)
        tcs=testCaseSeven(driver)
        startTime=time.time()
        url=tcs.launchTestCasePage()
        
        if "test_cases" not in url:
            assert False, "The test case page is not launched"

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
