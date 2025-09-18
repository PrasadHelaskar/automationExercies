from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseSeventeen(baseMethods):
    __private_crossButton=(By.CSS_SELECTOR, "a[class='cart_quantity_delete']")

    # Action Methods

    def clickCrossButton(self):
        self.click(self.__private_crossButton)