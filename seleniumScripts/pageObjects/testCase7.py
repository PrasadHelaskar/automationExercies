import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseSeven(baseMethods):
    __private_testCaseButton=(By.XPATH, "(//a[@href='/test_cases'])[1]")


    def launchTestCasePage(self) -> str:
        self.click(self.__private_testCaseButton)

        url=self.get_url()

        return url 