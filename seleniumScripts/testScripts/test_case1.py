import time
import pytest
from faker import Faker
from seleniumScripts.utils.logger import Logger
from seleniumScripts.pageObjects.testCase1 import testCaseOne
from seleniumScripts.testScripts.test_base import initialTest

log=Logger().get_logger(__name__)

class Test_caseOne():
    @pytest.mark.order(1)
    def test_caseOne(self,driver):
        initialTest().initialtest(driver)
        tco=testCaseOne(driver)
        faker=Faker('en_US')
        startTime=time.time()
        name=faker.name()
        email=faker.email()
        log.info("name %s",name)
        log.info("email %s",email)
        tco.signupActions(name,email)
        password="1234567890"
        tco.genderNamePasswordActions(name,password)

        tco.birthDayselection(23,4,2015)

        tco.consentsActions()
        
        firstname=faker.first_name()
        lastname=faker.last_name()
        address=faker.address()
        state=faker.state()
        city=faker.city()
        zipCode=faker.zipcode()
        mobileNumber=faker.phone_number()
        
        tco.addressActions(firstname,lastname,address,state,city,zipCode,mobileNumber)

        tco.CreatAccountActions(name)

        # tco.postAccountActions()

        endTime=time.time()

        log.info("Required Time: %s", (endTime-startTime))
