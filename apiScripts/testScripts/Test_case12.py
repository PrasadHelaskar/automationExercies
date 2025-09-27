import json
import pytest
from apiScripts.utils.logger import Logger
from apiScripts.utils.jsonOperations import jsonRead
from apiScripts.utils.baseMethods import BaseMethod

log=Logger().get_logger()
class Test_caseTweleve(BaseMethod):
    @pytest.mark.order(12)
    def test_caseTweleve(self,base_attribute):
        """
            DELETE METHOD To Delete User Account
        """
        url=base_attribute['url']+"/deleteAccount"

        body={
            "email": jsonRead("EMAIL"),
            "password": "123123123"
        }
        
        apiCall=self.delete_method(url=url,body=body,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))