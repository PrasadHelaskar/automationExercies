import time
import pytest
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase8 import testCaseEight
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseEight():
    @pytest.mark.order(6)
    def test_caseEight(self,driver):
        initialTest().initialtest(driver)
        tce=testCaseEight(driver)
        startTime=time.time()
        tce.visitProductDetailsPage()

        product=tce.getProductDetails()

        log.info("Name: %s",product['name'])
        log.info(product['category'])
        log.info("Price: %s",product['cost'])
        log.info("Quantity: %s",product['quantity'])
        log.info(product['availibility'])
        log.info(product['condition'])
        log.info(product['brand'])

        
        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
