import json
import pytest
from apiScripts.utils.logger import Logger
from apiScripts.utils.baseMethods import BaseMethod

log=Logger().get_logger()
class Test_caseSix(BaseMethod):
    @pytest.mark.order(6)
    def test_caseSix(self,base_attribute):
            
        url=base_attribute['url']+"/searchProduct"

        body={
            "search_product": "jean"
        }
        
        apiCall=self.post_method(url=url,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))