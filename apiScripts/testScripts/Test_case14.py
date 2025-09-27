import json
import pytest
from faker import Faker
from apiScripts.utils.logger import Logger
from apiScripts.utils.baseMethods import BaseMethod
from apiScripts.utils.jsonOperations import jsonRead

log=Logger().get_logger()
fake=Faker()
birthdate = fake.date_of_birth(minimum_age=18, maximum_age=60)
class Test_caseFouteen(BaseMethod):
    @pytest.mark.order(14)
    def test_caseFouteen(self,base_attribute):
        """
            GET user account detail by email
        """
        url=base_attribute['url']+"/getUserDetailByEmail"

        body={
                "email": jsonRead("EMAIL")
        }
        
        apiCall=self.get_method(url=url,params=body,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))