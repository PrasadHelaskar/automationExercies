import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase12 import testCaseTwelve
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseTwelve():
    @pytest.mark.order(6)
    def test_caseTwelve(self,driver):
        initialTest().initialtest(driver)
        tct=testCaseTwelve(driver)
        startTime=time.time()
        
        tct.openProductPage()

        for index in range(1,4):
            tct.addToCartOnHover(index)
            if index==3:
                tct.clickViewCart()
        
        script="""return document.querySelectorAll("[id*='product']").length;"""
        countFromWebpage=driver.execute_script(script)
        
        if countFromWebpage==tct.getProductCount():
            for productIndex in range(1,countFromWebpage+1):
                listOfDetails=tct.getDetails(productIndex)

                totalPrice=listOfDetails[0]*listOfDetails[1]

                if totalPrice!=listOfDetails[2]:
                    break
                else:
                    log.info(f"{totalPrice} matching with calcuations seen on webpage")

        else:
            log.warning(f"Count from Webpage {countFromWebpage} is not matching with recived count")

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))