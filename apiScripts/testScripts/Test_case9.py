import json
import pytest
from apiScripts.utils.logger import Logger
from apiScripts.utils.baseMethods import BaseMethod

log=Logger().get_logger()
class Test_caseNine(BaseMethod):
    @pytest.mark.order(9)
    def test_caseNine(self,base_attribute):
            
        url=base_attribute['url']+"/verifyLogin"

        body={
            "email": "your.email+fakedata31671@gmail.com",
            "password": "123123123"
        }
        
        apiCall=self.delete_method(url=url,body=body,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))