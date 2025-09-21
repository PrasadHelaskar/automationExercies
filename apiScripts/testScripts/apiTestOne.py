import json
import requests
import pytest
from apiScripts.utils.logger import Logger

log=Logger().get_logger()
class Test_caseOne():
    @pytest.mark.order(1)
    def test_caseOne(self,base_attribute):
            
        url=base_attribute['url']+"/productsList"
        
        apiCall=requests.get(url=url,timeout=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))