import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.testScripts.test_base import initialTest
from seleniumScripts.pageObjects.testCase21 import testCaseTwentyOne

log=Logger().get_logger(__name__)
faker=Faker()

class Test_caseTwentyOne():
    @pytest.mark.order(21)
    def test_caseTwentyOne(self,driver):
        initialTest().initialtest(driver)
        tcto=testCaseTwentyOne(driver)
        startTime=time.time()
        
        title=tcto.productPage()

        assert title.lower() == "All Products".lower() , "Ttile Didn't match"

        tcto.openProductDetailsPage()

        reviewerdate={
            "reviewerName": f"{faker.name()}",
            "reviewerEmail": f"{faker.email()}",
            "reviewerReview": f"{faker.paragraph(nb_sentences=1)}"
        }

        tcto.reviewerActions(reviewerdate)

        endTime=time.time()
        log.info("Required Time: %s", (endTime-startTime))