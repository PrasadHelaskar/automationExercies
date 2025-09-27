import json
import pytest
from apiScripts.utils.logger import Logger
from apiScripts.utils.baseMethods import BaseMethod

log=Logger().get_logger()
class Test_caseTwo(BaseMethod):
    @pytest.mark.order(2)
    def test_caseTwo(self,base_attribute):
        """
            POST To All Products List
        """
        url=base_attribute['url']+"/productsList"
        
        apiCall=self.post_method(url=url,time=5)

        log.info("Responce Code: %s",apiCall.status_code)

        assert apiCall.status_code == 200 , "Error: Status code didn't match"

        if apiCall.status_code == 200:
            responce=apiCall.json()

            log.info(json.dumps(responce,indent=4))