import json
import pytest
from faker import Faker
from apiScripts.utils.logger import Logger
from apiScripts.utils.baseMethods import BaseMethod
from apiScripts.utils.jsonOperations import jsonRead

log=Logger().get_logger()
fake=Faker()
birthdate = fake.date_of_birth(minimum_age=18, maximum_age=60)
class Test_caseEleven(BaseMethod):
    @pytest.mark.order(11)
    def test_caseEleven(self,base_attribute):
        """
            POST To Create/Register User Account
        """
        url=base_attribute['url']+"/createAccount"

        body={
                "name": fake.name(),
                "email": jsonRead("EMAIL"),
                "password": "123123123",
                "title": "Mrs",
                "birth_date": birthdate.day,
                "birth_month": birthdate.month,
                "birth_year": birthdate.year,
                "firstname": fake.first_name(),
                "lastname": fake.last_name(),
                "company": fake.company(),
                "address1": fake.street_address(),
                "address2": fake.secondary_address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.state(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
        }
        
        apiCall=self.post_method(url=url,body=body,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))