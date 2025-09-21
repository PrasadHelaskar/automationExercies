import time
from selenium.webdriver.common.by import By
from seleniumScripts.utils.baseMethods import baseMethods
from seleniumScripts.utils.logger import Logger

log=Logger().get_logger(__name__)

class testCaseTwentyFive(baseMethods):

    __private_topTitleText=(By.XPATH, "//div[@class='col-sm-6']/h2")
    
    __private_bottomSubscriptionTitleText=(By.XPATH, "//div[@class='single-widget']/h2")

    __private_scrollToTOpButton=(By.ID, "scrollUp")

    def getTextForTopTitle(self)-> str:
        text=self.get_text(self.__private_topTitleText)

        return text
    
    def getBottomSubscriptionTitleText(self):
        text=self.get_text(self.__private_bottomSubscriptionTitleText)

        return text
    
    def clickScrollToTOp(self):
        self.click(self.__private_scrollToTOpButton)