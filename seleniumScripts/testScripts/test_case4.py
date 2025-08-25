import json
import time
import pytest
import sys
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase4 import testCaseFour
from seleniumScripts.testScripts.test_base import initialTest

log= Logger().get_logger()

with open ("seleniumScripts/testData/testLoginData.json") as testFile:
    data=json.load(testFile)

class Test_caseFour():
    @pytest.mark.order(4)
    @pytest.mark.parametrize("credentials",[
        (data["valid_data"])
        # (data["invalid_data"])
    ]
)
    def test_caseTwo(self,driver,credentials):
        email = credentials["email"]
        password = credentials["password"]

        
        def login(driver,email,password):
            initialTest().initialtest(driver)
            tcf=testCaseFour(driver)
            startTime=time.time()

            tcf.loginActions(email=email,password=password)
            try:
                tcf.loginConfiremationActions()
            except Exception:
                log.info("Incorrct Credentials")
                return False
                
            tcf.postAccountActions()
            endtime=time.time()
            log.info("Required Time %s", (endtime-startTime))
            return True
    
        testTwoResult=login(driver,email,password)

        assert testTwoResult, "The test is failed "