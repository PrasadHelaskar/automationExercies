import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase19 import testCaseNinteen

log=Logger().get_logger(__name__)

class Test_caseNinteen():
    @pytest.mark.order(6)
    def test_caseNinteen(self,driver):
        initialTest().initialtest(driver)
        tcn=testCaseNinteen(driver)
        startTime=time.time()
        
        tcn.clickProductPage()

        tcn.clickMadame()

        title=tcn.BreandTitleText()
        
        assert title.lower() == "Brand - Madame Products".lower() , "THe Brand title ie not matching"

        tcn.clickPolo()
        
        title=tcn.BreandTitleText()
        
        assert title.lower() == "Brand - Polo Products".lower() , "THe Brand title ie not matching"

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))