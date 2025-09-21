import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase18 import testCaseEightteen 

log=Logger().get_logger(__name__)

class Test_caseEightteen():
    @pytest.mark.order(18)
    def test_caseEightteen(self,driver):
        initialTest().initialtest(driver)
        tce=testCaseEightteen(driver)
        startTime=time.time()
        tce.clickWomenCategory()
        tce.clickWomenSaree()

        categoryText=tce.categoryTitleText()

        assert categoryText.lower() == "Women - Saree Products".lower(), "The title is not matching"

        tce.clickManCategory()

        tce.clickManJeans()
        
        categoryText=tce.categoryTitleText()

        assert categoryText.lower() == "Men - Jeans Products".lower(), "The title is not matching"

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))