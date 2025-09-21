import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase13 import testCaseThirteen
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseThirteen():
    @pytest.mark.order(13)
    def test_caseThirteen(self,driver):
        initialTest().initialtest(driver)
        tct=testCaseThirteen(driver)
        startTime=time.time()
        
        tct.openProductPage()

        tct.openProductDetailsPage()

        tct.productCountAddition(4)

        tct.clickAddToCart()

        tct.clickViewCart()

        productDetails=tct.getDetails(1)

        if isinstance(productDetails, list):
            totalCalculatedPrice=productDetails[0]*productDetails[1]

            if totalCalculatedPrice==productDetails[2]:
                log.info("Calculated Price matched with thr seen on the webpage: %s",totalCalculatedPrice)
            else:
                log.error("Calculated Price doesn't match with thr seen on the webpage: %s",totalCalculatedPrice)

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))