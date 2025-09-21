import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase22 import testCaseTwentyTwo

log=Logger().get_logger(__name__)
faker=Faker()

class Test_caseTwentytwo():
    @pytest.mark.order(22)
    def test_caseTwentytwo(self,driver):
        initialTest().initialtest(driver)
        tctt=testCaseTwentyTwo(driver)
        startTime=time.time()
        title=tctt.scrollTillRecommendedItem()

        assert title.lower() == "recommended items".lower() , "Ttile didn't match"

        tctt.addItemToCart()

        script="""return document.querySelectorAll("[id*='product']").length;"""
        countFromWebpage=driver.execute_script(script)
        
        if countFromWebpage==tctt.getProductCount():
            for productIndex in range(1,countFromWebpage+1):
                listOfDetails=tctt.getDetails(productIndex)

                totalPrice=listOfDetails[0]*listOfDetails[1]

                if totalPrice!=listOfDetails[2]:
                    break
                else:
                    log.info(f"{totalPrice} matching with calcuations seen on webpage")

        else:
            log.warning(f"Count from Webpage {countFromWebpage} is not matching with recived count")
        
        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))