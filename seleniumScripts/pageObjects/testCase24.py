import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentyFour(baseMethods):
    __private_downloadInvoice=(By.CSS_SELECTOR, "a[href^='/download_invoice']")

    __private_deleteAccount=(By.CSS_SELECTOR, "a[href^='/delete_account']")
    
    __private_deleteConfirmation=(By.XPATH, "//h2[@data-qa='account-deleted']/..//b")

    __private_Continuebutton=(By.CSS_SELECTOR, "a[data-qa='continue-button']")

    # Action Methods

    def downloadInvoice(self):
        self.click(self.__private_downloadInvoice)
        time.sleep(15)

    def postAccountActions(self):
        self.click(self.__private_deleteAccount)

        assert self.get_text(self.__private_deleteConfirmation).lower() == "account deleted!" , "Account deletion failed"

        self.click(self.__private_Continuebutton)
